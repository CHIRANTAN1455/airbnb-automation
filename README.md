# Airbnb Reservation Automation

This project provides a script to automate the process of logging into Airbnb, extracting reservation data, and saving it to a local Excel file using Python and Selenium.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/airbnb-reservation-automation.git
    cd airbnb-reservation-automation
    ```

2. **Install the required Python packages:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Download the WebDriver:**

    Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) and ensure it's in your system's PATH or specify its location in the script.

## Usage

1. **Update Credentials:**

    Open the `airbnb_automation.py` file and update the `email` and `password` variables with your Airbnb login credentials.

2. **Run the script:**

    ```sh
    python airbnb_automation.py
    ```

3. **Output:**

    The script will save the reservation data to a file named `reservations.xlsx` in the project directory.

## Project Structure

airbnb-reservation-automation/
│
├── airbnb_automation.py # Main script for automating Airbnb reservation extraction
├── requirements.txt # List of dependencies
└── README.md # Project README file

## Features

- **Automated Login:** Logs into Airbnb using provided credentials.
- **Data Extraction:** Extracts reservation data including guest names, check-in, and check-out dates.
- **Excel Export:** Saves the extracted reservation data to a local Excel file.

## Dependencies

- [Selenium](https://pypi.org/project/selenium/): For browser automation.
- [pandas](https://pypi.org/project/pandas/): For data manipulation and Excel export.
- [openpyxl](https://pypi.org/project/openpyxl/): For Excel file handling.

Install the dependencies using the command:

```sh
pip install -r requirements.txt
Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes.
    Commit your changes (git commit -am 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgements

    Selenium Documentation
    pandas Documentation
    openpyxl Documentation

### Instructions to Add `requirements.txt`

To create the `requirements.txt` file, you can list the required dependencies:

```sh
echo selenium > requirements.txt
echo pandas >> requirements.txt
echo openpyxl >> requirements.txt
This README provides a clear guide on setting up and using the Airbnb reservation automation script. Make sure to replace placeholders like yourusername and update any URLs or file paths as necessary.
