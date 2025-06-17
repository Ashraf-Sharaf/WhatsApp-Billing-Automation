import logging
import time
import datetime
import pandas as pd
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from config import *

def send_whatsapp_messages():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding='utf-8'
    )

    lebanese_months = [
        "كانون الثاني", "شباط", "آذار", "نيسان", "أيار", "حزيران",
        "تموز", "آب", "أيلول", "تشرين الأول", "تشرين الثاني", "كانون الأول"
    ]

    current_date = datetime.datetime.now()
    start_time = time.time()

    df = pd.read_excel(EXCEL_FILE)

    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://web.whatsapp.com")

    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div'))
        )
        logging.info("QR code detected. Please scan the QR code to log in.")
        time.sleep(30)
    except TimeoutException:
        logging.info("Session found. Logged in automatically.")

    wait = WebDriverWait(driver, 30)

    successful_deliveries = 0
    total_messages = len(df) - 1

    for index, row in df.iloc[1:].iterrows():
        bill_number = row['رقم الفاتورة']
        name = row['اسم المشترك']
        old_meter = row[' العداد الحالي']
        new_meter = row['العداد السابق']
        difference = row['المصروف  بالكيلو واط']
        unit_price = row['سعر الكيلو واط']
        fixed_value = row['رسم الإشتراك']
        monthly_bill = row['بدل كهرباء شهري']
        debts = row['رصيد سابق']
        additional_expenses = row['مصاريف إضافية']
        final_bill = row['المجموع العام']
        phone_number = str(row['رقم الهاتف'])
        water = row['بدل مياه']
        waste = row['بدل نفايات']
        date = f"{lebanese_months[current_date.month - 1]} - {current_date.year}"

        message = (
            "كهرباء الخلوات\n"
            f"التاريخ: {date}\n"
            f"رقم الفاتورة: {bill_number}\n"
            f"اسم المشترك: {name}\n"
            f"العداد الحالي: {new_meter} | العداد السابق: {old_meter}\n"
            f"المصروف: {difference} | سعر الكيلو واط: {unit_price}\n"
            f"رسم الاشتراك: {fixed_value} | بدل كهرباء شهري: {monthly_bill}\n"
            f"ديون سابقة: {debts} | مصاريف إضافية: {additional_expenses}\n"
            f"المجموع : {final_bill}\n\n"
            f"رقم المحاسبة: {ACCOUNTING_NUMBER}\n"
            f"رقم الصيانة: {MAINTENANCE_NUMBER}\n"
            f"يمكنك الدفع في أي فرع Whish Money على رقم الحساب ({WHATSAPP_ACCOUNT_NUMBER})\n"
            f"أو الاتصال بالجابي {COLLECTOR_NAME} رقم هاتفه {COLLECTOR_PHONE}"
        )

        try:
            driver.get(f"https://web.whatsapp.com/send?phone={phone_number}")

            message_box = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]'))
            )

            pyperclip.copy('')
            message_box.clear()
            message_box.click()

            time.sleep(1)

            pyperclip.copy(message)
            message_box.send_keys(Keys.CONTROL, 'v')
            time.sleep(1)
            message_box.send_keys(Keys.ENTER)

            pyperclip.copy('')
            successful_deliveries += 1

            time.sleep(5)

        except Exception as e:
            pyperclip.copy('')
            logging.error(f"Failed to send message (#{bill_number}) to {name} ({phone_number}).")

    end_time = time.time()
    execution_time = end_time - start_time
    minutes = int(execution_time // 60)
    seconds = int(execution_time % 60)
    logging.error(f"Successfully delivered {successful_deliveries} out of {total_messages} messages")
    logging.error(f"Program executed in {minutes} minutes and {seconds} seconds.")
    logging.error("------------------------------------------------------------------------------------------------")

    driver.quit()
