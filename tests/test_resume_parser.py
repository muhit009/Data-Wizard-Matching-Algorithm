import unittest
from unittest.mock import patch, MagicMock
import os
from matching_algorithm.resume_parser import extract_text_from_pdf, parse_resume, extract_bullet_points, extract_summary, \
    extract_education, combine_resume_fields, process_resume


class TestResumeParser(unittest.TestCase):

    @patch('resume_parser.PyPDF2.PdfReader')
    def test_extract_text_from_pdf(self, mock_pdf_reader):
        # Mocking the PdfReader to return predefined text from PDF
        mock_page = MagicMock()
        mock_page.extract_text.return_value = "This is a test resume text."
        mock_pdf_reader.return_value.pages = [mock_page]

        pdf_path = 'test_resume.pdf'  # Mocked, not used since we're patching
        text = extract_text_from_pdf(pdf_path)

        # Check that the extracted text matches the mocked text
        self.assertEqual(text, "This is a test resume text.")

    def test_parse_resume(self):
        # Sample resume text for testing the parsing logic
        resume_text = """
        Summary: Software Engineer with 5 years of experience in Python and AI.
        Education: BSc Computer Science from XYZ University.
        Skills: Python, AI, Machine Learning.
        Experience: • Developed AI models. • Led team projects.
        Certifications: AWS Certified Solutions Architect.
        Projects: • Project A. • Project B.
        """
        parsed_data = parse_resume(resume_text)

        # Check that the parsed data contains the expected fields
        self.assertIn('summary', parsed_data)
        self.assertIn('education', parsed_data)
        self.assertIn('skills', parsed_data)
        self.assertIn('experience', parsed_data)
        self.assertIn('certifications', parsed_data)
        self.assertIn('projects', parsed_data)

        # Check that the extracted bullet points are in 'experience' and 'projects'
        self.assertIn('• Developed AI models', parsed_data['experience'])
        self.assertIn('• Project A', parsed_data['projects'])

    def test_extract_bullet_points(self):
        # Test input with bullet points
        text = "• Developed AI models\n• Led team projects"
        bullet_points = extract_bullet_points(text)

        # Check if the bullet points are correctly extracted
        self.assertEqual(bullet_points, "Developed AI models\nLed team projects")

        # Test input without bullet points
        text_no_bullet_points = "Developed AI models and led team projects."
        bullet_points_no_bullet = extract_bullet_points(text_no_bullet_points)

        # Check that it returns the same text if no bullet points are found
        self.assertEqual(bullet_points_no_bullet, "Developed AI models and led team projects.")

    def test_extract_summary(self):
        text = "Experienced software engineer with expertise in AI."
        summary = extract_summary(text)

        # Check that the summary matches the input
        self.assertEqual(summary, "Experienced software engineer with expertise in AI.")

        # Test when no summary is provided
        summary_empty = extract_summary("")
        self.assertEqual(summary_empty, "No summary available")

    def test_extract_education(self):
        text = "BSc in Computer Science from XYZ University."
        education = extract_education(text)

        # Check that the education matches the input
        self.assertEqual(education, "BSc in Computer Science from XYZ University.")

        # Test when no education is provided
        education_empty = extract_education("")
        self.assertEqual(education_empty, "No education information available")

    def test_combine_resume_fields(self):
        parsed_data = {
            'summary': "Experienced software engineer.",
            'education': "BSc in Computer Science.",
            'skills': "Python, Machine Learning",
            'experience': "Developed AI models.",
            'certifications': "AWS Certified.",
            'projects': "Project A, Project B."
        }

        combined_summary = combine_resume_fields(parsed_data)

        # Check that the combined summary contains all sections
        self.assertIn("Summary/Objective:", combined_summary)
        self.assertIn("Education:", combined_summary)
        self.assertIn("Skills:", combined_summary)
        self.assertIn("Experience:", combined_summary)
        self.assertIn("Certifications:", combined_summary)
        self.assertIn("Projects:", combined_summary)

    @patch('resume_parser.extract_text_from_pdf')
    @patch('resume_parser.parse_resume')
    @patch('resume_parser.combine_resume_fields')
    def test_process_resume(self, mock_combine_resume_fields, mock_parse_resume, mock_extract_text_from_pdf):
        # Mocking the functions involved in process_resume
        mock_extract_text_from_pdf.return_value = "Sample resume text."
        mock_parse_resume.return_value = {
            'summary': "Software Engineer",
            'education': "XYZ University",
            'skills': "Python",
            'experience': "Developed models"
        }
        mock_combine_resume_fields.return_value = "Summary/Objective: Software Engineer\nEducation: XYZ University\nSkills: Python\nExperience: Developed models"

        # Simulating the processing of a resume
        pdf_path = 'test_resume.pdf'
        summary_text = process_resume(pdf_path)

        # Check that the combined summary text is returned as expected
        self.assertEqual(summary_text,
                         "Summary/Objective: Software Engineer\nEducation: XYZ University\nSkills: Python\nExperience: Developed models")


if __name__ == '__main__':
    unittest.main()
