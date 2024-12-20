import pandas as pd

# Main function to clean rows based on Domain Status
def clean_invalid_domain_rows(file_path, output_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Ensure 'Domain Status' column exists
    if 'Domain Status' not in df.columns:
        print("Error: Missing 'Domain Status' column.")
        return
    
    # Remove rows with 'Invalid Domain' status
    df_cleaned = df[df['Domain Status'] != 'Invalid Domain']
    
    # Save the cleaned data
    df_cleaned.to_excel(output_path, index=False)
    print(f"Cleaning complete. Results saved to {output_path}.")

# Usage
input_file = "verified_domains.xlsx"  # Replace with your input Excel file path (with Domain Status)
output_file = "cleaned_emails.xlsx"   # Replace with your desired output file path

clean_invalid_domain_rows(input_file, output_file)
