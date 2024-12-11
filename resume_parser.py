import PyPDF2
import re
import os


# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text


# Function to parse different sections from the resume text
def parse_resume(text):
    # Define patterns for each section
    sections = {
        'summary': r"(summary|objective|profile|about)(.*?)(?=\n(education|skills|experience|certifications|projects|$))",
        'education': r"(education|academics|qualification|degree)(.*?)(?=(skills|experience|certifications|projects|$))",
        'skills': r"(technical skills|skills|key skills)(.*?)(?=(experience|education|certifications|projects|$))",
        'experience': r"(experience|work experience|employment history)(.*?)(?=(skills|education|certifications|projects|$))",
        'certifications': r"(certifications|certificates)(.*?)(?=(skills|education|experience|projects|$))",
        'projects': r"(projects|software engineering projects|personal projects)(.*?)(?=(skills|experience|certifications|education|$))"
    }

    parsed_data = {}

    for section, pattern in sections.items():
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            parsed_data[section] = match.group(2).strip()

    # Extract bullet points from experience and projects
    parsed_data['experience'] = extract_bullet_points(parsed_data.get('experience', ''))
    parsed_data['projects'] = extract_bullet_points(parsed_data.get('projects', ''))
    parsed_data['summary'] = extract_summary(parsed_data.get('summary', ''))
    parsed_data['education'] = extract_education(parsed_data.get('education', ''))

    return parsed_data


# Helper function to extract bullet points from sections
def extract_bullet_points(text):
    # This will extract lines that likely represent bullet points or important tasks
    bullet_points = []
    if text:
        bullet_points = re.findall(r"•\s*(.*?)\n|([^\n]+)", text)  # Looks for bullet points or lines
        bullet_points = [point[0] or point[1] for point in bullet_points]  # Clean up results
    return "\n".join(bullet_points).strip()


# Helper function to extract a complete summary
def extract_summary(text):
    # Match the summary section and return the complete summary
    if text:
        return text.strip()
    return "No summary available"


# Helper function to extract education details
def extract_education(text):
    # Match the education section and return the complete education details
    if text:
        return text.strip()
    return "No education information available"


# Function to combine parsed sections into a summary text
def combine_resume_fields(parsed_data):
    summary = []

    if 'summary' in parsed_data:
        summary.append(f"Summary/Objective:\n{parsed_data['summary']}")
    if 'education' in parsed_data:
        summary.append(f"Education:\n{parsed_data['education']}")
    if 'skills' in parsed_data:
        summary.append(f"Skills:\n{parsed_data['skills']}")
    if 'experience' in parsed_data:
        summary.append(f"Experience:\n{parsed_data['experience']}")
    if 'certifications' in parsed_data:
        summary.append(f"Certifications:\n{parsed_data['certifications']}")
    if 'projects' in parsed_data:
        summary.append(f"Projects:\n{parsed_data['projects']}")

    return '\n\n'.join(summary)


# Function to process the resume PDF and return the combined summary
def process_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    parsed_data = parse_resume(text)
    summary_text = combine_resume_fields(parsed_data)
    return summary_text


# Example usage
if __name__ == "__main__":
    pdf_path = "software_engineer_resume.pdf"  # Replace with the path to your resume PDF file
    resume_summary = process_resume(pdf_path)
    print(resume_summary)
