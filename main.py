import random
import smtplib
import datetime as dt
import re
from getpass import getpass

my_email = "reallybrianhudson@gmail.com"
password = getpass(prompt="Enter Password: ")
now = dt.datetime.now()
date_of_birth = dt.datetime(year=1981, month=11, day=27)


def email_message(sending_message, sending_quote_author):
    print("Starting SMTP")
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        print("logging in")
        connection.login(user=my_email, password=password)
        print("sending mail")
        connection.sendmail(
            from_addr="python@flight-crew.org",
            to_addrs=my_email,
            msg=f"Subject: Words of wisdom from {sending_quote_author}\n\n{sending_message}"
        )
    print("closing connection")


if now.weekday() == 2:
    with open("quotes.txt") as file:
        quotes_list = file.read().splitlines()
    random_quote = random.choice(quotes_list)
    # returns a Match object so we need the first element
    quote_author = re.search(r"(?<=(\ \-\ )).+", random_quote)
    email_message(random_quote, quote_author[0])
