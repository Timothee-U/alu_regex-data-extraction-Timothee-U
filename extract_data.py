#!/usr/bin/env python3
import re

# Regex patterns
EMAIL_PATTERN = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
URL_PATTERN = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?'
PHONE_PATTERN = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
CREDIT_CARD_PATTERN = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'

def extract_data(text, pattern):
    """Extracts and returns all matches for a given regex pattern."""
    return re.findall(pattern, text)

def main():
    with open("sample_text.txt", "r", encoding="utf-8") as file:
        content = file.read()

    extracted_data = {
        "Emails": extract_data(content, EMAIL_PATTERN),
        "URLs": extract_data(content, URL_PATTERN),
        "Phone Numbers": extract_data(content, PHONE_PATTERN),
        "Credit Card Numbers": extract_data(content, CREDIT_CARD_PATTERN),
    }

    for key, values in extracted_data.items():
        print(f"\n{key}:")
        for value in values:
            print(value)

if __name__ == "__main__":
    main()
