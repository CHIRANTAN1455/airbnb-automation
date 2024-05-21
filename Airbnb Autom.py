import requests
from bs4 import BeautifulSoup
import pandas as pd

# URLs and credentials
login_url = 'https://www.airbnb.com/login'
reservations_url = 'https://www.airbnb.com/reservations'
email = 'your_email'
password = 'your_password'

# Start a session
session = requests.Session()

# Login data
login_data = {
    'email': email,
    'password': password,
    # Add any additional form data required for login here
}

# Perform login
response = session.post(login_url, data=login_data)

# Check if login was successful
if 'Dashboard' in response.text:
    print('Login successful!')
else:
    print('Login failed.')
    exit()

# Fetch reservations page
response = session.get(reservations_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Parse reservations data
reservations = []
for reservation in soup.select('.reservation-class'):  # Update selector
    reservation_data = {
        'id': reservation.get('data-id'),
        'guest_name': reservation.select_one('.guest-name-class').text,
        'check_in': reservation.select_one('.check-in-class').text,
        'check_out': reservation.select_one('.check-out-class').text,
        # Add more fields as needed
    }
    reservations.append(reservation_data)

# Convert reservations to DataFrame
df = pd.DataFrame(reservations)

# Save to Excel file
output_file = 'reservations.xlsx'
df.to_excel(output_file, index=False)

print(f'Reservations saved to {output_file}')
