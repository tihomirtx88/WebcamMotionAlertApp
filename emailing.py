import smtplib
import os
from PIL import Image
from email.message import EmailMessage


from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv();

api_key = os.getenv("API_KEY");

def get_image_type(image_path):
    with Image.open(image_path) as img:
        return img.format.lower()

def send_email(image_path):
    email_message = EmailMessage();
    email_message["subject"] = "New customer show up!";
    email_message.set_content("Hey, we just saw new customer to in!");

    with open(image_path, "rb") as file:
        content = file.read();

    subtype = get_image_type(image_path)
    email_message.add_attachment(content, maintype="image", subtype=subtype)

    gmail =smtplib.SMTP("smtp.gmail.com", 587);
    gmail.ehlo();
    gmail.starttls();
    gmail.login("tihomirtx88@gmail.com", api_key);
    gmail.sendmail("tihomirtx88@gmail.com", "tihomirtx88@gmail.com", email_message.as_string());
    gmail.quit();

if __name__ == "__main__":
    send_email(image_path="images/19.png");