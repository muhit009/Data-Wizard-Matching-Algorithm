"""
Developer Name: Sai Sundeep Rayidi
Creation Date: 11/20/2024
Last Update Date: 11/30/2024

"""


import pandas as pd
import numpy as np


def load_data():
    # Load job datasets
    data1 = pd.read_csv('data/dataset1.csv')
    data2 = pd.read_csv('data/dataset2.csv')

    combined_records = np.vstack(
        (data1[["Job Title", "Job Description"]], data2[["position_title", "job_description"]]))

    combined_df = pd.DataFrame(combined_records, columns=["Job Title", "Job Description"])

    # Filter out short descriptions
    filtered_df = combined_df[combined_df["Job Description"].str.len() >= 600]

    return filtered_df
