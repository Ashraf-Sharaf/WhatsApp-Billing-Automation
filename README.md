# WhatsApp Billing Automation

## Project Description
This Python script automates sending personalized WhatsApp messages to multiple contacts by reading data from an Excel file. It uses Selenium WebDriver to interact with WhatsApp Web and sends custom billing messages in Arabic with Lebanese month names.

## Features
- Reads contact and billing data from Excel  
- Sends customized WhatsApp messages automatically  
- Logs errors and delivery status  
- Uses environment variables for sensitive info  
- Supports Arabic messages with Lebanese month formatting  

## Prerequisites
- Python 3.7 or higher  
- Google Chrome browser installed  
- WhatsApp account for QR code login  
- Excel file with required data columns  

## Project Structure
├── .env.example  
├── .env  
├── config.py  
├── main.py  
├── whatsapp_sender.py  
├── ExcelFile.xlsx  
├── requirements.txt  
├── README.md  
└── .gitignore  

## Excel File Format
make sure your excel file format is the same as the ExcelFile.xlsx

## Installation and Run
```bash
git clone https://github.com/Ashraf-Sharaf/WhatsApp-Billing-Automation.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
