import pandas as pd
import dns.resolver

# Validate domain existence
def is_valid_domain(email):
    domain = email.split('@')[-1]
    try:
        dns.resolver.resolve(domain, 'MX')  # Check for MX records
        return True
    except:
        return False

# Main function to verify email domains
def verify_email_domains(file_path, output_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Ensure required columns exist
    if 'Business Email' not in df.columns:
        print("Error: Missing 'Business Email' column.")
        return
    
    # Add Domain Status column
    df['Domain Status'] = df['Business Email'].apply(lambda email: "Valid Domain" if is_valid_domain(email) else "Invalid Domain")
    
    # Save the results with Domain Status
    df.to_excel(output_path, index=False)
    print(f"Domain verification complete. Results saved to {output_path}.")

# Usage
input_file = "emails.xlsx"  # Replace with your input Excel file path
output_file = "verified_domains.xlsx"  # Replace with your desired output file path

verify_email_domains(input_file, output_file)
