import torch
from transformers import DistilBertModel, DistilBertTokenizer
import pandas as pd
import json
from scipy.spatial.distance import cosine
import argparse
import numpy as np

# job categories are defined here for category matching to make sure relevant roles are only displayed
job_categories = {
    "IT": [
        "Software Developer", "Systems Analyst", "Network Administrator", "UX Designer",
        "Cloud Solutions Architect", "Cybersecurity Analyst", "Blockchain Developer", 
        "AI Research Scientist", "Mobile App Developer", "Data Engineer",
    ],
    "Design": [
        "Graphic Designer", "UX Designer", "Product Designer", "Creative Director"
    ],
    "Marketing": [
        "Marketing Specialist", "Content Marketing Manager", "SEO Strategist",
        "E-commerce Specialist", "Brand Manager", "Public Relations Specialist", "SEO Consultant"
    ],
    "Engineering": [
        "Electrical Engineer", "Mechanical Engineer", "Civil Engineer", "CAD Engineer"
    ],
    "Data Science": [
        "Data Scientist", "Statistical Analyst", "Data Engineer"
    ],
    "Business": [
        "Product Manager", "Business Analyst", "Operations Manager", "Risk Manager",
        "Compliance Officer", "Purchasing Manager", "Sales Associate", "Real Estate Agent"
    ],
    "Sales": [
        "Sales Associate", "Sales Director", "Pharmaceutical Sales Representative"
    ],
    "Human Resources": [
        "Human Resources Manager"
    ],
    "Customer Service": [
        "Customer Support Representative"
    ],
    "Quality Assurance": [
        "Quality Assurance Engineer", "Software Tester"
    ],
    "Supply Chain": [
        "Supply Chain Coordinator", "Logistics Analyst", "Logistics Coordinator"
    ],
    "Event Management": [
        "Event Manager"
    ],
    "Research": [
        "Research Scientist", "Clinical Research Coordinator", "Lab Technician", "Environmental Scientist"
    ],
    "Education": [
        "Educational Consultant", "Academic Advisor"
    ],
    "Finance": [
        "Financial Analyst", "Fintech Analyst"
    ],
    "Biotechnology": [
        "Biotechnologist", "Biomedical Engineer"
    ],
    "Language Services": [
        "Foreign Language Translator"
    ], 
    "Technical Writing": [
        "Technical Writer"
    ],
     "Law": [
        "Corporate Lawyer"
    ],
    "Video Game Industry": [
        "Video Game Designer", "3D Animator"
    ]
}



def get_category(job_title, categories, experience):
    possible_titles = [job_title]
    if experience >= 3:
        senior_title = "Senior " + job_title
        possible_titles.append(senior_title)
    
    for category, titles in categories.items():
        for title in possible_titles:
            if title in titles:
                return category
    return None


# input is received as Command Line Arguments 
parser = argparse.ArgumentParser(description='Job Recommendation System')
parser.add_argument('--location', type=str, required=True, help='Preferred job location')
parser.add_argument('--mode', type=str, required=True, choices=['remote', 'hybrid', 'onsite'], help='Preferred mode of work')
parser.add_argument('--experience', type=int, required=True, help='Candidate\'s experience in years')
parser.add_argument('--job_title', type=str, required=True, help='Preferred job title')
args = parser.parse_args()


resume = "parsed_data.json"
job_listings = "processed_data.csv"
distances = "geocoding_values.json"

#printing for debug
print("Resume data being loaded...")
with open(resume, 'r') as file:
    parsed_resume = json.load(file)
    print("Loaded successfully.")

#printing for debug
print("job listings being loaded...")
job_listing = pd.read_csv(job_listings)
print("Loaded successfully.")

#printing for debug
print("Distances being loaded...")
with open(distances, 'r') as file:
    distance_values = json.load(file)
    print(f" Loaded successfully with {len(distance_values)} entries.")

print("Model Initializing...")
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased').to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
print("Initialized successfully.")

def text_encoding(text):
    #print for debug
    print(f"Encoding text: {text[:30]}... (Larger texts take time)")
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True, padding='max_length').to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
    with torch.no_grad():
        return model(**inputs).last_hidden_state[:, 0, :].squeeze().cpu().numpy()

print("Encoding resume...")
encoded_skills = text_encoding(parsed_resume['skills'])
print("Skills encoded.")
encoded_experience = text_encoding(parsed_resume['experience'])
print("Experience encoded.")


recommendations = []
print("Beginning Job recommendation...")

userlocation_normalized = args.location.replace(' ', '_').lower()



for index, job in job_listing.iterrows():
    print(f"Processing job {index + 1}/{len(job_listing)}: ID {job['Job ID']}...")
    title_location_match_bonus = 0

    job_category = get_category(job['Job Title'], job_categories,0)
    userjob_category = get_category(args.job_title, job_categories,args.experience)

    if job_category != userjob_category:
        print(f"Job ID {job['Job ID']} skipped (category mismatch).")
        continue

    print("category match. Encoding job required skills...")
    job_requiredskills_encoding = text_encoding(job['Skills'])
    skills_similarity = 1 - cosine(encoded_skills, job_requiredskills_encoding)
    skills_similarity = round(skills_similarity, 2)
    print(f"Skills similarity calculated: {skills_similarity}")

    job_location_normalized = job['Location'].replace(' ', '_').lower()
    distance_key = f"{userlocation_normalized}_{job_location_normalized}"
    print(f"Looking up distance with key: {distance_key}")
    if userlocation_normalized == job_location_normalized:
            location_distance = 0  # Same city so we give the distance as 0
            print(f"Job is in the preferred location: {args.location}")
    else:
        distance_key = f"{userlocation_normalized}_{job_location_normalized}"
        print(f"Looking up distance with key: {distance_key}")
        location_distance = distance_values.get(distance_key, None)
    print(f"Distance found: {location_distance}")

    if location_distance is not None and location_distance <= 100:
        miles_distance = round(location_distance, 2)
        location_similarity = 1
       

    else:
        miles_distance = 'N/A'
        location_similarity = 0
        
        print(f"Job ID {job['Job ID']} skipped (location beyond 100 miles).")
        continue

    experience_check = 1 if abs(args.experience - job['Years of Experience']) <= 2 else 0
    experience_check = round(experience_check, 2)

    mode_check = 1 if job['Mode of Work'].lower() == args.mode else 0.5 if args.mode == 'hybrid' else 0
    mode_check = round(mode_check, 2)

    
    if job['Job Title'].lower() == args.job_title.lower() and job['Location'] == args.location and job['Mode of Work'] == args.mode:
        title_location_match_bonus = 10  # additional bonus to prioritize local jobs
    

    
    weighted_score = round(title_location_match_bonus+ 0.4 * skills_similarity + 0.2 * location_similarity + 0.2 * experience_check + 0.2 * mode_check, 2)


    recommendations.append({
        'Job ID': job['Job ID'],
        'Job Title': job['Job Title'],
        'Salary': job['Salary'],
        'Location': job['Location'],
        'Company Name': job['Company Name'],
        'Distance': miles_distance,
        'Score': weighted_score
    })
    print(f"Job ID {job['Job ID']} processed. Score: {weighted_score}")


if not recommendations:
    print("No jobs found.")
else:
    recommendations_data_frame = pd.DataFrame(recommendations)
    recommendations_data_frame = recommendations_data_frame.sort_values(by='Score', ascending=False)
    top_percentage_index = max(int(len(recommendations_data_frame) * 0.20), 10)
    top_recommendations_data_frame = recommendations_data_frame.head(top_percentage_index)

    #top recommendations are stored to a CSV file
    top_recommendations_data_frame.to_csv('recommendations.csv', index=False)
    print(f"Top recommendations saved !")
