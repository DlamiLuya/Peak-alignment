import pandas as pd

# Load the Excel file
file_path = 'Tota Data For blank subtraction.xlsx'  # replace with your file path
blank_subtr_df = pd.read_excel(file_path, sheet_name='my_sheet')

# Extract the sample name column and compound data separately
sample_names = blank_subtr_df.iloc[:, 0]  # First column with sample names
data = blank_subtr_df.iloc[:, 1:]  # All compound data (excluding sample names)

# Get baseline values for "20241029C travel blank Luyanda:1" (assuming it is the first row after headers)
baseline_values = data.iloc[0]  # Baseline values are the first row of compound data

# Perform blank subtraction for all samples, excluding the baseline row itself
subtracted_data = data.iloc[1:].subtract(baseline_values, axis=1).clip(lower=0)

# Combine sample names with the subtracted data
blank_subtracted_df = pd.concat([sample_names.iloc[1:].reset_index(drop=True), subtracted_data.reset_index(drop=True)], axis=1)

# Set column names to match original for clarity
blank_subtracted_df.columns = blank_subtr_df.columns

# Save to a new Excel file if needed
blank_subtracted_df.to_excel('blank_subtracted_output_Tota.xlsx', index=False)

# Show the first few rows of the result
print(blank_subtracted_df.head())


