#!/usr/bin/env python3
import re

# Regex patterns
EMAIL_PATTERN = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
URL_PATTERN = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?'
PHONE_PATTERN = r'(\(\d{3}\)\s?|\d{3}[-.]?)\d{3}[-.]\d{4}'
CREDIT_CARD_PATTERN = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
TIME_PATTERN = r'\b(?:[01]?\d|2[0-3]):[0-5]\d\b|\b(?:1[0-2]|0?[1-9]):[0-5]\d\s?(?:AM|PM)\b'
HTML_TAG_PATTERN = r'<[^>]+>'
HASHTAG_PATTERN = r'#\w+'
CURRENCY_PATTERN = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

def extract_data(text, pattern):
    return re.findall(pattern, text)

def main():
    with open("sample_text.txt", "r", encoding="utf-8") as file:
        content = file.read()

    extracted_data = {
        "Emails": extract_data(content, EMAIL_PATTERN),
        "URLs": extract_data(content, URL_PATTERN),
        "Phone Numbers": extract_data(content, PHONE_PATTERN),
        "Credit Card Numbers": extract_data(content, CREDIT_CARD_PATTERN),
        "Times": extract_data(content, TIME_PATTERN),
        "HTML Tags": extract_data(content, HTML_TAG_PATTERN),
        "Hashtags": extract_data(content, HASHTAG_PATTERN),
        "Currency Amounts": extract_data(content, CURRENCY_PATTERN),
    }

    for key, values in extracted_data.items():
        print(f"\n{key}:")
        for value in values:
            print(value)

if __name__ == "__main__":
    main()
