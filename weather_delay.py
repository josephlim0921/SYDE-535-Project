import pandas as pd
import numpy as np

def simulate_random_solution(dataframe):
    """Function to randomly select a row based on probabilities in df"""
    # Normalize the probability column to ensure it sums to 1
    dataframe['delay_probability'] = dataframe['delay_probability'] / dataframe['delay_probability'].sum()

    # Randomly choose a row based on the probability distribution
    selected_row = dataframe.sample(weights=dataframe['delay_probability'])
    return selected_row