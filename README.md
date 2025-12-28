# AutoExpire QR

AutoExpire QR is a Python automation project built using Streamlit.
It generates QR codes that automatically expire after a fixed time.

## Features
- QR code generation
- Countdown timer
- Auto expiry
- Regenerate QR code
- Token-based validation

## Technologies Used
- Python
- Streamlit
- qrcode
- uuid

## How It Works
1. User enters text or URL
2. System generates a QR code with a unique token
3. Countdown timer starts
4. QR expires automatically after time ends
5. New QR can be regenerated

## Installation
pip install streamlit qrcode[pil]

## Run Project
streamlit run app.py

## Project Type
Automation Project (Intermediate Level)

## Author
Shivani Chauhan

## Real Life Use Cases

- Temporary access links
- Event or seminar entry passes
- Secure document sharing
- Office visitor or meeting access
- Time-based automation practice
- 
## Work In Progress

I am currently working on adding more automation features such as:
- Email alert before QR code expiry
- Expiry notification messages
- Improved validation logic
