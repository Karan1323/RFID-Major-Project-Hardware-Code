import umail

def send_mail(rec_mail,reg_link):
    
    try:
        print('in send mail func. ')
        # Email details
        sender_email = 'rfidandnodemcu@gmail.com' # Replace with the email address of the sender
        sender_name = 'Karan' # Replace with the name of the sender
        sender_app_password = 'gtqaggseebzjmjkx' # Replace with the app password of the sender's email account
        recipient_email =rec_mail   # Replace with the email address of the recipient
        email_subject ='Registration Link ' # Subject of the email
        email_body=f'Click this link : {reg_link}'


        # Send the email
        # Connect to the Gmail's SSL port
        smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True)
        print('established connection to gmail')
        # Login to the email account using the app password
        smtp.login(sender_email, sender_app_password)
        print('logged into gmail account')
        # Specify the recipient email address
        smtp.to(recipient_email)
        # Write the email header
        smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
        smtp.write("Subject:" + email_subject + "\n")
        # Write the body of the email
        print(f'Received body as{reg_link}')
        smtp.write("\n"+ email_body+"\n")
        # Send the email
        smtp.send()
        # Quit the email session
        smtp.quit()
        
        return True
        
    except:
        print('Invalid email address')
        return False
