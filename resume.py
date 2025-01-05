# !pip install pdfminer.six
# !pip install spacy

import pdfminer
import re
from pdfminer.high_level import extract_text
import spacy

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    return extract_text(pdf_path)

def extract_name_from_resume(text):
    """Extracts a name from the resume text using regex."""
    pattern = r"(\b[A-Z][a-z]+\b)\s(\b[A-Z][a-z]+\b)"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_contact_number_from_resume(text):
    """Extracts a contact number from the resume text using regex."""
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_email_from_resume(text):
    """Extracts an email address from the resume text using regex."""
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_skills_from_resume(text, skills_list):
    """Extracts predefined skills from the resume text."""
    skills = [skill for skill in skills_list if re.search(rf"\b{re.escape(skill)}\b", text, re.IGNORECASE)]
    return skills

def extract_education_from_resume(text):
    """Extracts education information from the resume text using regex."""
    pattern = r"(?i)(?:Bsc|\bB\.\w+|\bM\.\w+|\bPh\.D\.\w+|\bBachelor(?:'s)?|\bMaster(?:'s)?|\bPh\.D)\s(?:\w+\s)*\w+"
    return re.findall(pattern, text)

def extract_data_science_education(text):
    """Extracts data science-related education using spaCy NLP."""
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    return [ent.text for ent in doc.ents if ent.label_ == 'ORG' and 'Data Science' in ent.text]

def extract_college_name(text):
    """Extracts the college name from the resume text."""
    lines = text.split('\n')
    college_pattern = r"(?i).*college.*"
    for line in lines:
        if re.match(college_pattern, line):
            return line.strip()
    return None

if __name__ == '__main__':
    pdf_path = r"C:\Users\HuTa0710\Downloads\Compressed\Resume-Parser-using-Python-main\Resume-Parser-using-Python-main\Untitled-resume.pdf"
    text = extract_text_from_pdf(pdf_path)
    
    # Extract and print the information
    name = extract_name_from_resume(text)
    print("Name:", name if name else "Name not found")

    contact_number = extract_contact_number_from_resume(text)
    print("Contact Number:", contact_number if contact_number else "Contact Number not found")

    email = extract_email_from_resume(text)
    print("Email:", email if email else "Email not found")

    skills_list = ['Python', 'Data Analysis', 'Machine Learning', 'Communication', 'Project Management', 'Deep Learning', 'SQL', 'Tableau']
    skills = extract_skills_from_resume(text, skills_list)
    print("Skills:", skills if skills else "No skills found")

    education = extract_education_from_resume(text)
    print("Education:", education if education else "No education information found")

    data_science_education = extract_data_science_education(text)
    print("Data Science Education:", data_science_education if data_science_education else "No data science education found")

    college_name = extract_college_name(text)
    print("College:", college_name if college_name else "College name not found")
