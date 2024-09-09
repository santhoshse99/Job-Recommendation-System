import pandas as pd
import numpy as np
import random

# Setting the random seed for reproducibility
np.random.seed(42)
num_entries = 10000

job_skills = {
    'Software Developer': [
        'Python', 'JavaScript', 'Java', 'C#', 'Go', 'TypeScript', 'Scala', 'Ruby', 'PHP',
        'Black Box Testing', 'Agile Testing', 'DevOps Practices', 'API Design', 'Microservices',
        'Spring Boot', 'Django', 'React', 'Angular', 'Vue.js', 'Cloud Services', 'AWS Lambda',
        'Containerization', 'Kubernetes', 'Docker', 'CI/CD', 'Git', 'SQL', 'NoSQL', 'GraphQL','AJAX','SDLC'
    ],
    'Microsoft CRM Developer': [
        'Javascript', 'C#', 'Microsoft Dynamics 365', 'ASP .NET', 'Canvas', 'Power BI',
        'PowerApps', 'Azure', 'SQL Server', 'Integration Services', 'Automated Testing', 'Custom Workflow Creation'
    ],
    'Database Developer': [
        'SQL Server', 'Microsoft Access', 'Oracle', 'MySQL', 'PostgreSQL', 'NoSQL Databases',
        'Database Design', 'Performance Tuning', 'ETL Processes', 'Data Warehousing', 'MongoDB', 'Cassandra'
    ],
    'Graphic Designer': [
        'Photoshop', 'Adobe Suite', 'Illustrator', 'InDesign', 'Sketch', 'Figma',
        'User Interface Design', 'Animation', 'Print Design', 'Web Design', 'Typography', 'Color Theory'
    ],
    'Systems Analyst': [
        'SQL', 'Networking', 'Linux', 'Cloud Computing', 'ERP Systems', 'System Architecture',
        'Data Analysis', 'Project Management', 'Information Security', 'Troubleshooting', 'SAP', 'Oracle Applications'
    ],
    'Product Manager': [
        'Project Management', 'Marketing', 'Public Speaking', 'SEO/SEM', 'Business Analysis',
        'Product Lifecycle Management', 'Market Research', 'User Experience Design', 'Data-Driven Decision Making', 'Agile Methodologies'
    ],
    'Sales Associate': [
        'Sales Techniques', 'Customer Service', 'E-commerce', 'CRM', 'Negotiation',
        'Salesforce', 'Lead Generation', 'Market Analysis', 'Product Presentation', 'Client Relationship Management'
    ],
    'Marketing Specialist': [
        'Digital Marketing', 'SEO/SEM', 'Content Creation', 'Social Media', 'Google Analytics',
        'Email Marketing', 'AdWords', 'Facebook Ads', 'Marketing Strategy', 'Brand Management', 'Campaign Management'
    ],
    'Data Scientist': [
        'Machine Learning', 'Data Analysis', 'Python', 'R', 'Statistical Analysis',
        'Deep Learning', 'TensorFlow', 'Keras', 'Data Mining', 'Big Data Technologies', 'Hadoop', 'Spark','Matplotlib', 'NumPy', 'Pandas', 'Seaborn', 'Scikit-learn', 'Jupyter Notebook', 'NLTK' ,
        'MS Visio', 'MS Excel', 'MS FrontPage',' MS Word'
   
    ],
    'Network Administrator': [
        'Networking', 'Cybersecurity', 'Linux', 'Cloud Computing', 'Docker',
        'Windows Server', 'Network Security', 'Cisco Systems', 'Firewall Management', 'VPN', 'Remote Support'
    ],
    'UX Designer': [
        'UI/UX Design', 'Sketch', 'Photoshop', 'InVision', 'User Research',
        'Prototype Design', 'User Testing', 'Interaction Design', 'Accessibility Design', 'Responsive Design','REST','SOAP','XML','JSON'
    ],
    'Technical Writer': [
        'Technical Documentation', 'Editing', 'Research', 'Content Management Systems', 'Proofreading',
        'API Documentation', 'User Manuals', 'Online Help Systems', 'Markdown', 'Technical Diagrams'
    ],
    'Cloud Solutions Architect': [
        'Cloud Computing', 'AWS', 'Azure', 'Google Cloud', 'Docker', 'Kubernetes',
        'Cloud Security', 'Cloud Migration', 'Hybrid Cloud', 'Serverless Architectures', 'Cloud Storage Solutions'
    ],
    'Cybersecurity Analyst': [
        'Cybersecurity', 'Ethical Hacking', 'Network Security', 'Cryptography', 'Firewalls',
        'Intrusion Detection', 'Malware Analysis', 'Risk Assessment', 'Security Audits', 'Compliance'
    ],
    'Blockchain Developer': [
        'Blockchain', 'Solidity', 'Ethereum', 'Cryptocurrency', 'Smart Contracts',
        'DApp Development', 'Truffle Framework', 'Hyperledger', 'Blockchain Architecture', 'Token Economics'
    ],
    'AI Research Scientist': [
        'Machine Learning', 'Deep Learning', 'TensorFlow', 'Python', 'AI Ethics',
        'Natural Language Processing', 'Computer Vision', 'Reinforcement Learning', 'AI Model Optimization', 'AI Applications'
    ],
    'Mobile App Developer': [
        'Mobile Development', 'Swift', 'Kotlin', 'React Native', 'Firebase',
        'iOS Development', 'Android Development', 'Mobile UI/UX Design', 'Cross-Platform Development', 'App Store Optimization'
    ],
    'DevOps Engineer': [
        'CI/CD', 'Scripting', 'Linux', 'Docker', 'Kubernetes',
        'Automation Tools', 'Jenkins', 'Ansible', 'Cloud Deployment', 'Monitoring and Logging', 'Security Best Practices'
    ],
    'Corporate Lawyer': [
        'Contract Law', 'Corporate Governance', 'M&A', 'Compliance', 'Litigation',
        'Intellectual Property', 'Labor Law', 'Securities Regulation', 'Corporate Finance Law', 'Dispute Resolution'
    ],
    'Environmental Scientist': [
        'Environmental Analysis', 'Sustainability', 'GIS', 'Ecology', 'Pollution Control',
        'Environmental Policy', 'Conservation Strategies', 'Waste Management', 'Water Quality Assessment', 'Environmental Impact Analysis'
    ],
    'Human Resources Manager': [
        'Employee Relations', 'Benefits Administration', 'Recruitment', 'Compliance', 'Training',
        'Performance Management', 'HR Policies', 'Workforce Planning', 'Employee Engagement', 'Diversity and Inclusion'
    ],
    'Public Health Official': [
        'Epidemiology', 'Biostatistics', 'Health Education', 'Public Policy', 'Community Health',
        'Disease Prevention', 'Public Health Surveillance', 'Global Health Issues', 'Health Promotion Programs', 'Emergency Response'
    ],
    'Biomedical Engineer': [
        'Biomechanics', 'Biomaterials', 'Medical Imaging', 'Tissue Engineering', 'Biomedical Devices',
        'Medical Instrumentation', 'Regenerative Medicine', 'Clinical Engineering', 'Biomolecular Engineering', 'Healthcare Technologies'
    ],
    '3D Animator': [
        '3D Modeling', 'Animation', 'Texturing', 'Rigging', 'Motion Capture',
        'Character Animation', 'Visual Effects', '3D Rendering', 'Animation Software', 'Storyboarding'
    ],
    'Real Estate Agent': [
        'Property Management', 'Sales', 'Real Estate Economics', 'Customer Service', 'Negotiation',
        'Real Estate Marketing', 'Property Appraisal', 'Market Analysis', 'Leasing Agreements', 'Property Law'
    ],
    'Fintech Analyst': [
        'Financial Modeling', 'Blockchain', 'Python', 'Machine Learning', 'Regulatory Knowledge',
        'Quantitative Analysis', 'Risk Management', 'Financial Markets', 'Cryptocurrency Analysis', 'Payment Systems'
    ],
    'Web Developer': [
        'HTML', 'CSS', 'JavaScript', 'PHP', 'Ruby on Rails','flask'
        'React.js', 'Angular', 'Node.js', 'Web Performance Optimization', 'Security Practices'
    ],
    'Video Game Designer': [
        'Game Mechanics', 'Storytelling', 'Programming', 'Graphic Design', 'User Interface Design',
        'Game Development Engines', 'Level Design', 'Game Testing', 'Player Psychology', 'Interactive Storytelling'
    ],
    'Logistics Coordinator': [
        'Supply Chain Management', 'Logistics Planning', 'Warehouse Operations', 'Inventory Management', 'Shipping',
        'Freight Management', 'Logistics Software', 'Supply Chain Optimization', 'Distribution Strategies', 'Import/Export Compliance'
    ],
    'Foreign Language Translator': [
        'Language Proficiency', 'Translation', 'Localization', 'Interpreting', 'Cultural Awareness',
        'Simultaneous Translation', 'Technical Translation', 'Document Translation', 'Multilingual Communication', 'Language Services'
    ],
    'SEO Consultant': [
        'SEO', 'Google Analytics', 'Content Marketing', 'Keyword Research', 'Webmaster Tools',
        'Link Building', 'SEO Strategy', 'Content Optimization', 'Search Engine Algorithms', 'Local SEO'
    ],
    'Data Security Analyst': [
        'Information Security', 'Network Security', 'Vulnerability Assessment', 'Encryption', 'Firewalls',
        'Penetration Testing', 'Security Operations', 'Incident Response', 'Data Privacy', 'Compliance Standards',
        'MS Visio', 'MS Excel', 'MS FrontPage',' MS Word'
    ],
    'Software Tester': [
        'Test Automation', 'Manual Testing', 'Performance Testing', 'Security Testing', 'Quality Assurance',
        'Selenium', 'Test Planning', 'Bug Tracking', 'Regression Testing', 'Test Scripts', 'Black Box Testing (Advanced)', 'Agile Testing (Experienced)', 'Retesting & Regression Testing'
    ],
    'Data Engineer': [
        'Data Integration', 'Data Warehousing', 'Big Data Technologies', 'Data Modeling', 'ETL Development',
        'SQL', 'Python', 'Apache Spark', 'Data Pipeline Construction', 'Real-time Data Processing',
        'MS Visio', 'MS Excel', 'MS FrontPage',' MS Word'
    ],
    'Data Analyst': [
        'Python', 'R', 'SQL', 'Tableau', 'Power BI', 'Excel', 
        'Pandas', 'NumPy', 'Statistical Analysis', 'Data Visualization', 'Machine Learning',
        'MS Visio', 'MS Excel', 'MS FrontPage',' MS Word'
    ],
    'Programmer Analyst': [
        'Java', 'C++', 'SQL', 'Python', 'System Analysis', 'Debugging','DBMS',
        'Code Optimization', 'Database Management', 'Software Development Lifecycle', 'Agile Methodologies'
    ],
    'Salesforce Developer': [
        'Apex', 'Visualforce', 'Salesforce Object Query Language (SOQL)', 'Lightning Components',
        'Salesforce APIs', 'CRM', 'Integration Patterns', 'Workflow Automation', 'Custom UI Development', 'Platform Development'
    ],
    'SAP Consultant': [
        'SAP ERP', 'SAP Business Suite', 'ABAP', 'NetWeaver', 'SAP HANA', 'SAP Fiori',
        'Business Process Knowledge', 'Data Migration', 'SAP Modules Specific Knowledge (like FI, MM, SD)', 'Project Management'
    ],
    
    'Cloud Engineer': [
        'AWS', 'Azure', 'Google Cloud', 'Docker', 'Kubernetes', 
        'Cloud Security', 'DevOps', 'CI/CD Pipelines', 'Server Management', 'Scripting'
    ],
    'Project Manager': [
        'Project Planning', 'Risk Management', 'Agile Scrum Master', 'Stakeholder Management', 
        'Budgeting', 'MS Project', 'Team Leadership', 'Performance Tracking', 'Resource Allocation', 'Communication Skills'
    ],
    'Quality Assurance Engineer': [
        'Test Automation', 'Selenium WebDriver', 'Quality Control Procedures', 'Bug Tracking Tools', 
        'JIRA', 'Regression Testing', 'Performance Testing', 'Test Plan Development', 'CI/CD', 'Security Testing'
    ],
    'Machine Learning Engineer': [
        'Python', 'TensorFlow', 'PyTorch', 'Scikit-learn', 'Data Modeling', 
        'Neural Networks', 'Deep Learning', 'NLP', 'Computer Vision', 'AI Algorithm Development'
    ],
    'DevOps Specialist': [
        'Jenkins', 'Ansible', 'Docker', 'Kubernetes', 'Terraform', 
        'Scripting (Bash/Python)', 'Linux', 'CI/CD Pipelines', 'Cloud Services', 'Monitoring Tools (Prometheus/Grafana)'
    ],
    'User Experience Designer': [
        'Sketch', 'InVision', 'User Research', 'Personas', 'Wireframing', 
        'Prototyping', 'Usability Testing', 'Interaction Design', 'Information Architecture', 'Visual Design'
    ],
    'Network Engineer': [
        'Routing and Switching', 'Firewalls', 'Cisco Systems', 'Juniper', 'Network Security',
        'WAN/LAN', 'VoIP', 'MPLS', 'Network Management Tools', 'Troubleshooting'
    ],
    'Business Analyst': [
        'Requirement Gathering', 'Data Analysis', 'Business Process Modeling', 'Stakeholder Analysis',
        'UML', 'SQL', 'Power BI', 'Tableau', 'SDLC', 'Agile Methodologies','Microsoft Office Suite (Word, PowerPoint, Excel)', 'Access', 'SQL', 'Tableau', 'Python', 'MS Power BI', 'KNIME','Hadoop',
'PySpark', 'Agile', 'Google Analytics', 'R programming language', 'Microsoft AZURE', 'generative AI', 'data analytics'
    ]
}

work_modes = ['Remote', 'Hybrid', 'Onsite']

# Helper function to select skills based on the job title
def generate_skills(job_title):
    # Removing the prefixes to match the base job title in the dictionary
    base_title = job_title.replace('Senior ', '').replace('Executive ', '')
    return ', '.join(random.sample(job_skills[base_title], min(len(job_skills[base_title]), random.randint(3, 5))))


# Defining job titles and companies
job_titles = list(job_skills.keys())

companies = [
    'TechCorp', 'DesignHub', 'SysWork', 'ProductPros', 'SalesForce', 'MarketHigh', 'DataTrend', 'NetSolutions', 
    'CreativeUX', 'WriteIt', 'GreenTech Innovations', 'Quantum Solutions', 'BlueSky Technologies', 'Pioneer Works', 
    'EcoSystems', 'NextGen Developers', 'AlphaBuild', 'Innovative Tech Solutions', 'Future Horizons',
    'CloudNet Systems', 'DataDriven Insights', 'BioTech Health', 'MediTech Solutions', 'Bright Futures',
    'Quantalytics', 'AstroTech', 'CryptoLogic', 'Digital Dreams', 'Urban Dynamics', 'SkyHigh Networks',
    'GreenLeaf Technologies', 'Oceanic Ventures', 'Pixel Graphics', 'DevStudios', 'Visionary Apps',
    'Pathfinder Enterprises', 'Streamline Studios', 'CapitalTech', 'Golden Ratio Enterprises', 'Vortex Dynamics',
    'Catalyst Creations', 'Infinity Game Studios', 'Nova Enterprises', 'Orbit Innovations', 'Beacon Hill Technologies',
    'CodeCrafters', 'TechBridge', 'Rainbow Designs', 'UrbanTech', 'Agile Development Co.', 'Gemini Solutions',
    'Quantum Realty', 'Solar Flare Studios', 'Lunar Landscapes', 'Celestial Systems', 'New Dawn Technologies',
    'Ethereal Arts', 'Vivid Visions', 'Radiant Solutions', 'Pulse Point Media', 'Nebula Web Solutions',
    'Stellar Support Services', 'Platinum Enterprises', 'GoldenGate Tech', 'Silicon Valley Data Systems', 
    'Starlight Media', 'Titan Tech', 'Aurora Analytics', 'Crown Computing', 'Velvet Ventures',
    'Ironclad Tech', 'Jade Services', 'Pegasus Properties', 'Zephyr Innovations', 'Mystic Tech',
    'Echo Enterprises', 'Oasis Outsourcing', 'Nova Mechanics', 'Orion Solutions', 'Digital Dynamo',
    'Momentum Technologies', 'Crimson Technology', 'Cascade Communications', 'Quantum Web Development', 
    'Peak Performance Systems', 'Summit Securities', 'Chronos Technology', 'Elite Operations', 'Marble Media',
    'Springboard Solutions', 'Lighthouse Logistics', 'Terra Firma Technologies', 'SpireTech', 'Mirage Media',
    'Paramount Tech', 'Zenith Solutions', 'New Horizons Systems', 'Pinnacle Platforms', 'Cobalt Tech',
    'Omega Mobile', 'Phoenix Enterprises', 'Shadowfax Technologies', 'Twilight Technologies', 'Guardian Tech',
    'Iris Innovations', 'Sapphire Systems', 'Ruby Radiance', 'Emerald Enterprises', 'Diamond Dynamics'
]

# Define locations
locations = [
    "Montgomery, AL", "Birmingham, AL", "Huntsville, AL",
    "Anchorage, AK", "Fairbanks, AK", "Juneau, AK",
    "Phoenix, AZ", "Tucson, AZ", "Mesa, AZ",
    "Little Rock, AR", "Fayetteville, AR", "Fort Smith, AR",
    "Los Angeles, CA", "San Francisco, CA", "San Diego, CA",
    "Denver, CO", "Colorado Springs, CO", "Aurora, CO",
    "Hartford, CT", "New Haven, CT", "Stamford, CT",
    "Dover, DE", "Wilmington, DE", "Newark, DE",
    "Tallahassee, FL", "Miami, FL", "Orlando, FL",
    "Atlanta, GA", "Savannah, GA", "Augusta, GA",
    "Honolulu, HI", "Hilo, HI", "Kailua, HI",
    "Boise, ID", "Idaho Falls, ID", "Nampa, ID",
    "Chicago, IL", "Springfield, IL", "Peoria, IL",
    "Indianapolis, IN", "Fort Wayne, IN", "Evansville, IN",
    "Des Moines, IA", "Cedar Rapids, IA", "Davenport, IA",
    "Topeka, KS", "Wichita, KS", "Overland Park, KS",
    "Frankfort, KY", "Louisville, KY", "Lexington, KY",
    "Baton Rouge, LA", "New Orleans, LA", "Shreveport, LA",
    "Augusta, ME", "Portland, ME", "Lewiston, ME",
    "Annapolis, MD", "Baltimore, MD", "Rockville, MD",
    "Boston, MA", "Worcester, MA", "Springfield, MA",
    "Lansing, MI", "Detroit, MI", "Grand Rapids, MI",
    "Saint Paul, MN", "Minneapolis, MN", "Rochester, MN",
    "Jackson, MS", "Gulfport, MS", "Biloxi, MS",
    "Jefferson City, MO", "Kansas City, MO", "Saint Louis, MO",
    "Helena, MT", "Billings, MT", "Missoula, MT",
    "Lincoln, NE", "Omaha, NE", "Bellevue, NE",
    "Carson City, NV", "Las Vegas, NV", "Reno, NV",
    "Concord, NH", "Manchester, NH", "Nashua, NH",
    "Trenton, NJ", "Newark, NJ", "Jersey City, NJ",
    "Santa Fe, NM", "Albuquerque, NM", "Las Cruces, NM",
    "Albany, NY", "New York, NY", "Buffalo, NY",
    "Raleigh, NC", "Charlotte, NC", "Greensboro, NC",
    "Bismarck, ND", "Fargo, ND", "Grand Forks, ND",
    "Columbus, OH", "Cleveland, OH", "Cincinnati, OH",
    "Oklahoma City, OK", "Tulsa, OK", "Norman, OK",
    "Salem, OR", "Portland, OR", "Eugene, OR",
    "Harrisburg, PA", "Philadelphia, PA", "Pittsburgh, PA",
    "Providence, RI", "Warwick, RI", "Cranston, RI",
    "Columbia, SC", "Charleston, SC", "Greenville, SC",
    "Pierre, SD", "Sioux Falls, SD", "Rapid City, SD",
    "Nashville, TN", "Memphis, TN", "Knoxville, TN",
    "Austin, TX", "Houston, TX", "Dallas, TX",
    "Salt Lake City, UT", "Provo, UT", "West Valley City, UT",
    "Montpelier, VT", "Burlington, VT", "Rutland, VT",
    "Richmond, VA", "Virginia Beach, VA", "Norfolk, VA",
    "Olympia, WA", "Seattle, WA", "Spokane, WA",
    "Charleston, WV", "Huntington, WV", "Morgantown, WV",
    "Madison, WI", "Milwaukee, WI", "Green Bay, WI",
    "Cheyenne, WY", "Casper, WY", "Laramie, WY"
]


data = []
for _ in range(num_entries):
    job_title = random.choice(list(job_skills.keys()))
    years_experience = random.randint(0, 20)

    # Appending 'Senior' to the job title based on experience
    if years_experience > 10:
        job_title = f'Executive {job_title}'
    elif years_experience > 5:
        job_title = f'Senior {job_title}'

    salary = f'${random.randint(150000, 250000)}' if years_experience > 8 else f'${random.randint(40000, 149999)}'

    data.append({
        'Job ID': _ + 1,
        'Job Title': job_title,
        'Salary': salary,
        'Skills': generate_skills(job_title),
        'Location': random.choice(locations),
        'Years of Experience': years_experience,
        'Company Name': random.choice(companies),
        'Mode of Work': random.choice(work_modes)
    })

# Converting to DataFrame
df = pd.DataFrame(data)

# Defining the file path for saving the CSV
file_path = '/Users/santh/Desktop/CS 787 Final Project/Random_Job_Data.csv'

# Saving the DataFrame to a CSV file
df.to_csv(file_path, index=False)
df = pd.read_csv(file_path)

# Converting the DataFrame to a JSON format
json_data = df.to_json(orient='records', lines=False)

# Specifying the path for the JSON output file to be saved.
json_file_path = '/Users/santh/Desktop/CS 787 Final Project/jsoninput_jobdata.json'

# Write the JSON data to a file
with open(json_file_path, 'w') as file:
    file.write(json_data)
