import smtplib
import pandas as pd
from email.message import EmailMessage

# Step 1: Configuration
EMAIL_ADDRESS = 'ramankms767@gmail.com'        # Your Gmail address
EMAIL_PASSWORD = 'your-app-password'          # Use Gmail App Password
CSV_FILE = 'contacts.csv'                     # CSV with HR contacts
RESUME_FILE = 'resume.pdf'                    # Your resume file

# Step 2: Read CSV File
contacts = pd.read_csv(CSV_FILE)

# Step 3: Create Email Template
def send_email(to_email, name):
    msg = EmailMessage()
    msg['Subject'] = 'Job Application for DevOps Engineer'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg.set_content(f'''
    Dear {name},

    I hope this email finds you well. I am applying for the DevOps Engineer role.
    Please find my attached resume for your reference.

    Looking forward to your response.

    Best regards,
    Raman K.
    ''')

    # Attach resume
    with open(RESUME_FILE, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

    # Step 4: Send Email using Gmail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print(f"Email sent to {to_email}")

# Step 5: Loop through contacts and send emails
for index, row in contacts.iterrows():
    send_email(row['email'], row['name'])
