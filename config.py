import os
from dotenv import load_dotenv

load_dotenv()

EXCEL_FILE = os.getenv("EXCEL_FILE", "ExcelFile.xlsx")
LOG_FILE = os.getenv("LOG_FILE", "whatsapp_message_log.txt")
WHATSAPP_ACCOUNT_NUMBER = os.getenv("WHATSAPP_ACCOUNT_NUMBER")
ACCOUNTING_NUMBER = os.getenv("ACCOUNTING_NUMBER")
MAINTENANCE_NUMBER = os.getenv("MAINTENANCE_NUMBER")
COLLECTOR_NAME = os.getenv("COLLECTOR_NAME")
COLLECTOR_PHONE = os.getenv("COLLECTOR_PHONE")
