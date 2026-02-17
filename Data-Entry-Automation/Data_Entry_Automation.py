from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

glink = 'https://forms.gle/CKzUTHdaybdnsXva8'
from bs4 import BeautifulSoup
from selenium import webdriver

import requests

response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
soup = BeautifulSoup(response.content, 'html.parser')

data_links = soup.find_all(name='a', attrs={'class': 'property-card-link'})
data_prices = soup.find_all(name='span', attrs={'class': 'PropertyCardWrapper__StyledPriceLine'})
data_address = soup.find_all(name='address')

Links = [tag.get('href') for tag in data_links]
Prices = [tag.getText().split('/')[0].replace('+', '').replace('1bd', '').replace('1 bd', '').strip() for tag in
          data_prices]
Address = [tag.getText().strip().replace('\n', '').replace('|', '') for tag in data_address]

Chrome_options = Options()
Chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=Chrome_options)
wait = WebDriverWait(driver, 10)

for i in range(len(Links)):
    driver.get(glink)
    time.sleep(3)

    add_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_input = driver.find_element(By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    add_input.send_keys(Address[i])
    price_input.send_keys(Prices[i])
    link_input.send_keys(Links[i])
    submit.click()
    time.sleep(2)



