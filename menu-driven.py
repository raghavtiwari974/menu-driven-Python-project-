import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def show_menu():
    print("\n📱 SocialComm Automator - Menu")
    print("1. Send SMS")
    print("2. Make a Phone Call")
    print("3. Post on LinkedIn")
    print("4. Post on Twitter (X)")
    print("5. Post on Facebook")
    print("6. Post on Instagram")
    print("7. Send WhatsApp Message")
    print("8. Send Email")
    print("9. Exit")

def send_sms():
    print("Sending SMS...")  # Add Twilio code here

def make_call():
    print("Making Phone Call...")  # Add Twilio code here

def post_linkedin():
    print("Posting on LinkedIn...")  # Add LinkedIn API code here

def post_twitter():
    print("Posting on Twitter (X)...")  # Add Twitter API code here

def post_facebook():
    print("Posting on Facebook...")  # Add Facebook API code here

def post_instagram():
    print("Posting on Instagram...")  # Add Instagram API or automation

def send_whatsapp():
    print("Sending WhatsApp Message...")  # Add Twilio WhatsApp code

def send_email():
    print("Sending Email...")

    sender_email = input("Enter your email: ")
    password = input("Enter your email password (App Password if Gmail): ")
    receiver_email = input("Enter receiver's email: ")
    subject = input("Enter subject: ")
    message = input("Enter your message: ")

    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter your choice (1–9): ")

        if choice == "1":
            send_sms()
        elif choice == "2":
            make_call()
        elif choice == "3":
            post_linkedin()
        elif choice == "4":
            post_twitter()
        elif choice == "5":
            post_facebook()
        elif choice == "6":
            post_instagram()
        elif choice == "7":
            send_whatsapp()
        elif choice == "8":
            send_email()
        elif choice == "9":
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice. Please try again.")
