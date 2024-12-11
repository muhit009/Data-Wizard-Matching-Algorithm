# JobScout.AI

## Project Description

**JobScout.AI** is an AI-powered job-matching platform that streamlines the job application process by matching job seekers with the most relevant job descriptions based on their uploaded resumes. The platform leverages unsupervised machine learning techniques, such as **K-Means clustering** and **Cosine Similarity**, along with **Natural Language Processing (NLP)**, to analyze both job descriptions and resumes to determine the best matches. 

### Key Features:
- **Resume Parsing:** Job seekers can upload their resumes in PDF format, which are parsed to extract key information such as summary, education, skills, experience, certifications, and projects.
- **Job Matching:** The system matches the extracted resume data against a dataset of job descriptions and ranks the jobs based on similarity.
- **Transparency:** The platform offers clear explanations of the matching scores between a job description and the uploaded resume, allowing users to understand why they are a good match.

### Technologies Used:
- Python
- **NLP Libraries:** NLTK, Spacy
- **Machine Learning Libraries:** scikit-learn, K-means clustering, cosine similarity
- **Resume Parsing:** PyPDF2, Regular Expressions
- **Embedding Models:** Sentence Transformers

---

## How the Matching Algorithm Works

The **JobScout.AI** algorithm consists of the following steps:

1. **Data Loading and Preprocessing:**
   - Job descriptions are loaded from datasets (`dataset1.csv` and `dataset2.csv`), and a preprocessing pipeline is applied to clean and prepare the text for matching.
   - Preprocessing includes tokenization, stopword removal, and lemmatization.
   - The job descriptions are then vectorized into numerical embeddings using the **Sentence-Transformers** model (`all-MiniLM-L6-v2`).

2. **Resume Parsing and Embedding:**
   - The user uploads a resume in PDF format, which is parsed using **PyPDF2** to extract the text.
   - The resume text is then processed similarly to job descriptions, extracting sections such as summary, skills, education, and experience.
   - The processed resume is vectorized into embeddings using the same model as job descriptions.

3. **Job Matching:**
   - The system computes the cosine similarity between the resume embedding and all job description embeddings.
   - The **K-Nearest Neighbors (KNN)** algorithm is used to find the top K most similar job descriptions based on their cosine similarity scores.
   - The top K results are returned with job titles, descriptions, and matching scores.

---

## Running the Project Locally

### Prerequisites:
Before running the project, ensure you have the following installed:

- **Python 3.8+**
- **pip** (Python's package installer)

### Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/jobscout-ai.git
   cd jobscout-ai

2. Install the required dependencies:
    ```bash
        pip install -r requirements.txt
        
        Ensure you have a resume like software_engineer_resume.odf in the current drectory and execute -
        python main.py
    ```
   
3. Sample output (JSON format):
    ```JSON
[
    {
        "job_title": "Software Engineer",
        "job_description": "Develop and maintain software solutions with a focus on AI and machine learning.",
        "matching_score": 0.8745
    },
    {
        "job_title": "Data Scientist",
        "job_description": "Analyze large datasets and build machine learning models for predictive analytics.",
        "matching_score": 0.8632
    },
] 
    ```

### Running Unit Tests:

1. Navigate to the tests/ directory:
    >>> cd tests
2. Run the unit tests:
    >>> python -m unittest discover


### Sample Use Case
    Let's say you're applying for a Machine Learning Engineer role and you upload your resume. The system will extract key information from your resume, such as your skills in Python, Machine Learning, and AI, then compare this data to a dataset of job descriptions. The system will return a list of the top K job titles and descriptions that best match your resume, allowing you to apply to positions that align with your qualifications.

    Example:

    You upload your resume for a Software Engineer position.
    The system returns top 5 job descriptions related to AI and Machine Learning roles.
    
    The results might look like:
        AI Engineer: "Develop AI solutions for business."
        Data Scientist: "Design machine learning models to improve product analytics."
        AI Engineer: "Work on cutting-edge AI models in healthcare."
    
    By following the steps, you can directly apply to jobs that best match your skill set.