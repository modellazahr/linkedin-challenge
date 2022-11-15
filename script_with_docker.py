from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
import random
from time import sleep, time

"""
This script create new user in Linkedin. Firstly you should run another script 'create_temp.py'
"""


def set_chrome_options():
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_prefs = {}
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options


fake = Faker()

name_last = fake.name().split()
name, last = [name_last[0], name_last[1]] if len(name_last) == 2 else [name_last[1], name_last[2]]

user_data = {
    'name': name,
    'lastname': last,
    'password': ''.join([i+str(random.randint(10, 100)) for i in last]),
    'email': 'enter_email_here'
}

driver = webdriver.Chrome(ChromeDriverManager().install(), options=set_chrome_options())


def human_type(xpath, word):
    """
    Type like human
    """
    form = driver.find_element(By.XPATH, xpath)
    for i in word:
        form.send_keys(i)
        sleep(random.uniform(0.2, 0.5))


url = 'https://www.linkedin.com/uas/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'

driver.get(url)

if user_data['email'] == 'enter_email_here':
    print('Please run script "create_temp.py" and get the email')
    user_data['email'] = input('Please enter it here ...')

if user_data['email'] == '':
    driver.close()
    import sys
    sys.exit()

sleep(3)

driver.find_element(By.XPATH, '//*[@id="join_now"]').click()

# driver.find_element(By.XPATH, '//*[@id="email-address"]').send_keys(user_data['email'])
human_type('//*[@id="email-address"]', user_data['email'])

# driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(user_data['password'])
human_type('//*[@id="password"]', user_data['password'])

driver.get_screenshot_as_file('screen_1.png')

driver.find_element(By.XPATH, '//*[@id="join-form-submit"]').click()

print('[+] Successfully entered your email and password')

sleep(3)

# driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys(user_data['name'])
human_type('//*[@id="first-name"]', user_data['name'])

# driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys(user_data['lastname'])
human_type('//*[@id="last-name"]', user_data['lastname'])

driver.get_screenshot_as_file('screen_2.png')

driver.find_element(By.XPATH, '//*[@id="join-form-submit"]').click()

print('[+] Successfully entered your name and lastname')

sleep(10)

driver.find_element(By.XPATH, '//*[@id="ember10"]').click()

# driver.find_element(By.XPATH, '//*[@id="typeahead-input-for-title"]').send_keys('Manager')
human_type('//*[@id="typeahead-input-for-title"]', 'Manager')

human_type('//*[@id="typeahead-input-for-company"]', 'Microsoft')

driver.get_screenshot_as_file('screen_3.png')

driver.find_element(By.XPATH, '//*[@id="ember15"]').click()

print('[+] Successfully entered your job and place of work')

sleep(5)


def listen_to_file():
    import os
    time_limit = 3600  # one hour from now.
    now = time()
    check_interval = 10  # seconds between checking for the file.
    last_time = time_limit + now
    file_needed = 'linked_in.txt'
    while time() <= last_time:
        if os.path.exists(f'All Mails/{file_needed}'):
            return True
        else:
            sleep(check_interval)


if listen_to_file():
    with open('All Mails/linked_in.txt', 'r') as file:
        for line in file.readlines():
            if len(line.strip()) == 6:
                user_data['secret_em'] = line.strip()
                break

human_type('//*[@id="email-confirmation-input"]', user_data['secret_em'])

driver.find_element(By.XPATH, '//*[@id="ember39"]').click()

print('[+] Successfully passed the mail check')

sleep(2)

driver.get('https://www.linkedin.com/feed/')

sleep(10)

print(f'[+] The user was successfully created, here is his data:\n'/
      f'email: {user_data["email"]}\n password: {user_data["password"]}\n'
      f'name: {user_data["name"]}\n lastname: {user_data["lastname"]}\n')

sleep(10)

driver.close()
