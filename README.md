# WhatsApp Bulk Message Sender Automation

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

## Installation

```bash
git clone https://github.com/yourusername/whatsapp-bulk-sender.git
cd whatsapp-bulk-sender
python -m venv venv
source venv/bin/activate    
pip install -r requirements.txt
