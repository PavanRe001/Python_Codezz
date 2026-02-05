import smtplib
from bs4 import BeautifulSoup
import requests
import os,time
import time
import random
from dotenv import load_dotenv

load_dotenv()
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
]

password = os.getenv("PASSWORD")
email = os.getenv('EMAIL')
sender = os.getenv('SENDER')

user_input = input('Enter the URL of the website to set price tracker (default = https://amzn.in/d/05e7SFKr): ')
URL = user_input or 'https://www.amazon.in/Casio-Enticer-Analog-Watch-MTP-VD01D-2EVUDF-A1364/dp/B07BS3LCP1/ref=sr_1_6?crid=32PDN34VVKAV2&dib=eyJ2IjoiMSJ9.dwTQXeKKnrSYp2enI0gFK5CNbnJ5L1lSISswOQo4UdYG8MDBO0KbW72hHfNE3nQx51HO1M5_PCCMke02hJkb9dWOENeXxeGA4z-e-VpD1mqSA6qb9jGo4ahwMZAJNFjZVFeHdd8WG7tqcB07_w3QDQpXMue1MKzHNcPH9FOCwfym64jIaAnK-mHQt2ovcEMGeBwFzAixJGfXrnCQH2r-3Val8Z-jgX_1xsCTaLrdr_NShNLpfIjHYKa7yUOeiw7rH5jhnYtRWP-lACn5HgNrwOFMhn2qoEX_xpS810Ivpv8.Kmarn8iL8CRqmBUg3m4bZFpeW_ydLmi32Rne1nEmNkk&dib_tag=se&keywords=fossil%2Bwatch%2Bblue&qid=1770273131&sprefix=fossil%2Bwatch%2Bblue%2Caps%2C354&sr=8-6&th=1'
Price_input = input('Enter the expected price for the product (press Enter for auto-detect ₹500 below current): ')

headers = {
    "User-Agent": random.choice(user_agents),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br"
}

try:
    time.sleep(random.uniform(2, 5))
    response = requests.get(url=URL, headers=headers, timeout=10, allow_redirects=True)

    if response.status_code == 503 or response.status_code == 429:
        print("Too many requests")
        exit()

    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    product_title = soup.find('span', id='productTitle')

    if not product_title:
        print("Too many requests")
        exit()

    clean_title = " ".join(product_title.get_text().split())
    print(clean_title)

    price_element = soup.find('span', class_='a-price-whole')

    if not price_element:
        print("Too many requests")
        exit()

    price_text = price_element.get_text().strip().replace(',', '').replace('.', '')
    current_price = float(price_text)

    if Price_input.strip():
        Price_expected = float(Price_input)
    else:
        Price_expected = current_price - 500

    print(f"Current Price: ₹{current_price}")
    print(f"Expected Price: ₹{Price_expected}")

    if current_price <= Price_expected:
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=email, password=password)
                message = f'Subject: Price Alert!!\n\n{clean_title} is now ₹{current_price}\n{URL}'.encode('utf-8')
                connection.sendmail(from_addr=email, to_addrs=sender, msg=message)
            print('Mail sent successfully')
        except:
            print("Configure your mail credentials correctly")
    else:
        print(f"Price ₹{current_price} is still above expected ₹{Price_expected}")

except:
    print("Too many requests")
