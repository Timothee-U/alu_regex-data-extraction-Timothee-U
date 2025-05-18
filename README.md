# Regex Data Extraction Project

## Overview
This project uses **Python** and **Regular Expressions (Regex)** to extract specific types of data from a text file. It can detect and extract:

- Email Addresses  
- URLs  
- Phone Numbers  
- Credit Card Numbers

## Technologies Used
- Python 3.x  
- Regular Expressions (`re` module)

## How to Use This Project

### 1. Clone the Repository
Replace `yourusername` with your GitHub username:
```bash
git clone https://github.com/yourusername/alu_regex-data-extraction-yourusername.git
```

### 2. Open the Project Folder
```bash
cd alu_regex-data-extraction-yourusername
```

### 3. Make Sure Python is Installed
Check your Python version:
```bash
python --version
```

### 4. Review the Sample File
Open `sample_text.txt`. This file already contains text with:
- Emails
- Links
- Phone numbers
- Credit card numbers  
(So you don’t need to add anything unless you want to test more.)

### 5. Run the Program
This will print the extracted data:
```bash
python extract_data.py
```

---

## Example: What’s Inside the Sample File

`sample_text.txt` includes:
```
Please contact us at support@example.com or info.company@domain.co.uk.
Visit our site: https://www.example.com or https://subdomain.example.org/page.
Phone: (123) 456-7890, 123-456-7890, 123.456.7890.
Card: 1234 5678 9012 3456 or 1234-5678-9012-3456.
Time: 14:30 and 2:30 PM.
Tags: <p>, <div class="example">, <img src="...">.
Hashtags: #Regex #Python
Price: $19.99 or $1,234.56.
```

---

## Example Output
When you run the script, you’ll see:
```
Emails:
support@example.com
info.company@domain.co.uk

URLs:
https://www.example.com
https://subdomain.example.org/page

Phone Numbers:
(123) 456-7890
123-456-7890
123.456.7890

Credit Card Numbers:
1234 5678 9012 3456
1234-5678-9012-3456
```

---

## Notes on Edge Cases
- Works with or without "www" in URLs
- Accepts multiple phone formats
- Handles emails with dots, plus signs, and subdomains
- Detects card numbers with spaces or dashes
