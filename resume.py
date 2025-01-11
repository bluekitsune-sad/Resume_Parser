# !pip install pdfminer.six
# !pip install spacy

from pdfminer.high_level import extract_text
import re
import json


class ResumeParser:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = self.extract_text_from_pdf()
        self.packet_json = {}

    def extract_text_from_pdf(self):
        try:
            return extract_text(self.pdf_path)
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return ""

    def extract_name(self):
        pattern = r"(\b[A-Z][a-z]+\b)\s(\b[A-Z][a-z]+\b)"
        match = re.search(pattern, self.text)
        self.packet_json['name'] = match.group() if match else None

    def extract_contact_number(self):
        pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
        match = re.search(pattern, self.text)
        self.packet_json['contact_number'] = match.group() if match else None

    def extract_email(self):
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        match = re.search(pattern, self.text)
        self.packet_json['email'] = match.group() if match else None

    def extract_skills(self, skills_list):
        skills = [skill for skill in skills_list if re.search(rf"\b{re.escape(skill)}\b", self.text, re.IGNORECASE)]
        self.packet_json['skills'] = skills if skills else None

    def extract_education(self):
        pattern = r"(?i)(?:Bsc|\bB\.\w+|\bM\.\w+|\bPh\.D\.\w+|\bBachelor(?:'s)?|\bMaster(?:'s)?|\bPh\.D)\s(?:\w+\s)*\w+"
        education = [match.strip() for match in re.findall(pattern, self.text)]
        self.packet_json['education'] = education if education else None

    def extract_college_name(self):
        lines = self.text.split('\n')
        college_pattern = r"(?i).*college.*"
        for line in lines:
            if re.match(college_pattern, line):
                self.packet_json['college'] = line.strip()
                return
        self.packet_json['college'] = None

    def parse(self, skills_list):
        self.extract_name()
        self.extract_contact_number()
        self.extract_email()
        self.extract_skills(skills_list)
        self.extract_education()
        self.extract_college_name()

    def get_packet_json(self):
        return self.packet_json


if __name__ == '__main__':
    pdf_path = r"/content/resume/resum.pdf"
    skills_list = ['Python', 'Data Analysis', 'Machine Learning', 'Communication',
                   'Project Management', 'Deep Learning', 'SQL', 'Tableau']

    parser = ResumeParser(pdf_path)
    parser.parse(skills_list)

    packet_json = parser.get_packet_json()
    print("Extracted Data as JSON:")
    print(json.dumps(packet_json, indent=4))
