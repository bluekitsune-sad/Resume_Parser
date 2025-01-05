from pdfminer.high_level import extract_text
# !pip install pdfminer.six
# !pip install spacy


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


if __name__ == '__main__':
    print(extract_text_from_pdf(r"C:\Users\HuTa0710\Downloads\Compressed\Resume-Parser-using-Python-main\Resume-Parser-using-Python-main\Untitled-resume.pdf"))

import pdfminer
import re


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


def extract_name_from_resume(text):
    name = None

    # Use regex pattern to find a potential name
    pattern = r"(\b[A-Z][a-z]+\b)\s(\b[A-Z][a-z]+\b)"
    match = re.search(pattern, text)
    if match:
        name = match.group()

    return name


if __name__ == '__main__':
    text = extract_text_from_pdf(r"C:\Users\HuTa0710\Downloads\Compressed\Resume-Parser-using-Python-main\Resume-Parser-using-Python-main\Untitled-resume.pdf")
    name = extract_name_from_resume(text)

    if name:
        print("Name:", name)
    else:
        print("Name not found")


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


def extract_contact_number_from_resume(text):
    contact_number = None

    # Use regex pattern to find a potential contact number
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    if match:
        contact_number = match.group()

    return contact_number


if __name__ == '__main__':
    text = extract_text_from_pdf(r"C:\Users\HuTa0710\Downloads\Compressed\Resume-Parser-using-Python-main\Resume-Parser-using-Python-main\Untitled-resume.pdf")
    contact_number = extract_contact_number_from_resume(text)

    if contact_number:
        print("Contact Number:", contact_number)
    else:
        print("Contact Number not found")


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


def extract_email_from_resume(text):
    email = None

    # Use regex pattern to find a potential email address
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    if match:
        email = match.group()

    return email


if __name__ == '__main__':
    text = extract_text_from_pdf(r"C:\Users\HuTa0710\Downloads\Compressed\Resume-Parser-using-Python-main\Resume-Parser-using-Python-main\Untitled-resume.pdf")
    email = extract_email_from_resume(text)

    if email:
        print("Email:", email)
    else:
        print("Email not found")


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


def extract_skills_from_resume(text, skills_list):
    skills = []

    # Search for skills in the resume text
    for skill in skills_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            skills.append(skill)

    return skills


if __name__ == '__main__':
    text = extract_text_from_pdf(r"C:\Users\HuTa0710\Downloads\Compressed\Resume-Parser-using-Python-main\Resume-Parser-using-Python-main\Untitled-resume.pdf")

    # List of predefined skills
    skills_list = ['Python', 'Data Analysis', 'Machine Learning', 'Communication', 'Project Management',
                   'Deep Learning', 'SQL', 'Tableau']

    extracted_skills = extract_skills_from_resume(text, skills_list)

    if extracted_skills:
        print("Skills:", extracted_skills)
    else:
        print("No skills found")


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


def extract_education_from_resume(text):
    education = []

    # Use regex pattern to find education information
    pattern = r"(?i)(?:(?:Bachelor|B\.S\.|B\.A\.|Master|M\.S\.|M\.A\.|Ph\.D\.)\s(?:[A-Za-z]+\s)*[A-Za-z]+)"
    matches = re.findall(pattern, text)
    for match in matches:
        education.append(match.strip())

    return education


if __name__ == '__main__':
    text = extract_text_from_pdf(r"C:\Users\HuTa0710\Downloads\Compressed\Resume-Parser-using-Python-main\Resume-Parser-using-Python-main\Untitled-resume.pdf")

    extracted_education = extract_education_from_resume(text)
    if extracted_education:
        print("Education:", extracted_education)
    else:
        print("No education information found")


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


def extract_education_from_resume(text):
    education = []

    # Use regex pattern to find education information
    pattern = r"(?i)(?:Bsc|\bB\.\w+|\bM\.\w+|\bPh\.D\.\w+|\bBachelor(?:'s)?|\bMaster(?:'s)?|\bPh\.D)\s(?:\w+\s)*\w+"
    matches = re.findall(pattern, text)
    for match in matches:
        education.append(match.strip())

    return education


if __name__ == '__main__':
    text = extract_text_from_pdf(r"C:\Users\HuTa0710\Downloads\Compressed\Resume-Parser-using-Python-main\Resume-Parser-using-Python-main\Untitled-resume.pdf")

    extracted_education = extract_education_from_resume(text)
    if extracted_education:
        print("Education:", extracted_education)
    else:
        print("No education information found")

import spacy

nlp = spacy.load('en_core_web_sm')


def extract_data_science_education(text):
    doc = nlp(text)

    education = []

    for ent in doc.ents:
        if ent.label_ == 'ORG' and 'Data Science' in ent.text:
            education.append(ent.text)

    return education


if __name__ == '__main__':
    text = extract_text_from_pdf(r"C:\Users\HuTa0710\Downloads\Compressed\Resume-Parser-using-Python-main\Resume-Parser-using-Python-main\Untitled-resume.pdf")

    extracted_education = extract_data_science_education(text)
    if extracted_education:
        print("Data Science Education:", extracted_education)
    else:
        print("No data science education found")


def extract_college_name(text):
    lines = text.split('\n')
    college_pattern = r"(?i).*college.*"
    for line in lines:
        if re.match(college_pattern, line):
            return line.strip()
    return None

    # Example usage:
    text = extract_text_from_pdf(r"C:\Users\HuTa0710\Downloads\Compressed\Resume-Parser-using-Python-main\Resume-Parser-using-Python-main\Untitled-resume.pdf")


college_name = extract_college_name(text)
if college_name:
    print("College:", college_name)
else:
    print("College name not found.")


