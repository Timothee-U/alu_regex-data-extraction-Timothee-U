# Regex Data Extraction Project

## Overview
This project extracts specific types of data from text using Regular Expressions (Regex) in Python.

### Extracted Data Types:
- Email Addresses
- URLs
- Phone Numbers (US formats)
- Credit Card Numbers
- Time (12-hour and 24-hour)
- HTML Tags
- Hashtags
- Currency Amounts

## Technologies Used
- Python 3
- Regex (`re` module)

## Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/YourUsername/alu_regex-data-extraction-YourUsername.git
cd alu_regex-data-extraction-YourUsername
```

2. **Ensure Python is Installed**
```bash
python3 --version
```

3. **Run the Script**
```bash
python3 extract_data.py
```

## Sample Data File (sample_text.txt)
The sample file includes all required data formats such as:
- Emails like `user@example.com`
- URLs like `https://www.example.com`
- Phone numbers like `(123) 456-7890`
- Credit card numbers like `1234 5678 9012 3456`
- Time like `14:30` and `2:30 PM`
- HTML tags like `<p>` and `<img src="image.jpg">`
- Hashtags like `#example`
- Currency like `$19.99`

## Output Example
When you run the script, it prints extracted values like:
```
Emails:
user@example.com
firstname.lastname@company.co.uk

URLs:
https://www.example.com
https://subdomain.example.org/page

...
```
