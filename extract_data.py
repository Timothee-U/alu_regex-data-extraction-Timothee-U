#!/usr/bin/env python3
import re

# Regex patterns
EMAIL_PATTERN = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
URL_PATTERN = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?'
PHONE_PATTERN = r'\+?250[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{3}|\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
CREDIT_CARD_PATTERN = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'

# New patterns:
# Time (24-hour e.g. 14:30 or 12-hour e.g. 2:00 PM)
TIME_PATTERN = r'\b((1[0-9]|2[0-3]|0?[0-9]):[0-5][0-9]\s?(AM|PM|am|pm)?)\b'

# Hashtags (#word, #Word123)
HASHTAG_PATTERN = r'#\w+'

# Currency ($ with optional commas and decimals)
CURRENCY_PATTERN = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

# HTML tags (<tag> or <tag attr="value">)
HTML_PATTERN = r'<[^>]+>'

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
        "Time": [match[0] for match in extract_data(content, TIME_PATTERN)],  # Extract full match
        "Hashtags": extract_data(content, HASHTAG_PATTERN),
        "Currency Amounts": extract_data(content, CURRENCY_PATTERN),
        "HTML Tags": extract_data(content, HTML_PATTERN),
    }

    for key, values in extracted_data.items():
        print(f"\n{key}:")
        for value in values:
            print(value)

if __name__ == "__main__":
    main()
