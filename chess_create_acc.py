from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import string
import time


def generate_random():
    with open("names.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        first_line = lines[0].strip()

    special_characters = string.punctuation.replace("`", "").replace("|", "").replace(":", "")
    special_char = random.choice(special_characters)
    number = random.randint(1, 9999)
    username = f"{first_line}{number}{number}"
    email = f"{username}@gmail.com"
    password = f"{number}{username}{special_char}"
    if len(password) < 8:
        password = f"{number}{username}{3 * special_char}"

    # Removes first line from names.txt
    remove = True
    if remove:
        with open("names.txt", "w", encoding="utf-8") as f:
            for line in lines[1:]:
                f.write(line)

    return email, password, username


def click(browser, xpath):
    button = WebDriverWait(browser, 10).until(
        ec.element_to_be_clickable((By.XPATH, xpath)))
    button.click()
    time.sleep(2)


def send(browser, xpath, variable):
    inputt = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, xpath)))
    inputt.send_keys(variable)
    time.sleep(2)


def create_account(email, password, username):
    try:
        chrome_options = Options()
        chrome_options.headless = False
        chrome_options.add_argument("--log-level=3")
        service = ChromeService(executable_path=r"C:\Users\alper\Downloads\chromedriver.exe")
        browser = webdriver.Chrome(service=service, options=chrome_options)
        browser.get("https://www.chess.com/register")
        click(browser, '/html/body/div[1]/div/div[3]/main/div/div/button')
        click(browser, '/html/body/div[1]/div/div[3]/main/div/form/div[1]/div[4]/label')
        click(browser, '/html/body/div[1]/div/div[3]/main/div/form/div[1]/button')
        send(browser, '//*[@id="registration_email"]', email)
        send(browser, '//*[@id="registration_password"]', password)
        click(browser, '/html/body/div[1]/div/div[3]/main/div/form/div[2]/button')
        send(browser, '/html/body/div[1]/div/div[3]/main/div/form/div[3]/div/div[1]/div[1]/input', username)
        click(browser, '/html/body/div[1]/div/div[3]/main/div/form/div[3]/div/div[2]/button')
        click(browser, '/html/body/div[1]/div/div[3]/div/div/div/button')
        click(browser, '/html/body/div[1]/div/div[3]/div/div/div/button')
        click(browser, '/html/body/div[1]/div/div[3]/div/div/div/button')
        click(browser, '/html/body/div[1]/div/div[3]/div/div/div/div/button[3]')
        click(browser, '/html/body/div[1]/div/div[3]/div/div/div/div/button[2]')

        acc_path = r"C:\Users\alper\OneDrive\Masaüstü\codes\Python ornekleri\selenium\chess\chess_accs.txt"
        with open(acc_path, "a", encoding="utf-8") as file:
            file.write(f"{email} {password} {username}\n")

        print("Hesap başarıyla oluşturuldu.")
    except Exception as e:
        print("Bilinmeyen bir hata meydana geldi. Hesap oluşturulamadı.", e)


email, password, username = generate_random()
print(email, password, username)

create_account(email, password, username)
