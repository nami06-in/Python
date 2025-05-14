import os
import smtplib
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

URL = "https://camelcamelcamel.com/"
MY_EMAIL = os.environ["MY_EMAIL"]
BUY_PRICE = 4000

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,ml;q=0.8",
    "Dnt": "1",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 "
                  "Safari/537.36",
  }

response = requests.get(url=URL, headers=header)
web_page_contents = response.text
soup = BeautifulSoup(web_page_contents, "html.parser")

price_with_comma = soup.find(name="span", class_="a-offscreen").getText().split("₹")[1]
price = float(price_with_comma.replace(",", ""))

if price < BUY_PRICE:
    title = soup.find(name="span", id="productTitle").getText().strip()
    # title = soup.find(name="span", id="productTitle").getText().split()
    # title = " ".join(title)
    contents = f'"{title}" is now ₹{price}\n{URL}'

    with smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, os.environ["MY_EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert\n\n{contents}".encode('utf-8')
        )
    print("SUCCESSFUL!!!")
