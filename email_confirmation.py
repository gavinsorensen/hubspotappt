import smtplib

def send_email_confirmation(customer_email, appointment_date):
    """
    Sends an email confirmation to the customer once their appointment has been successfully scheduled.

    Parameters:
    customer_email (str): Email address of the customer
    appointment_date (str): Date of the scheduled appointment

    Returns:
    None
    """
    # Establish a secure session with gmail's outgoing SMTP server using SMTP_SSL()
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Login to the email account from which the confirmation email will be sent
    smtp_server.login("sender@gmail.com", "password")

    # Compose the email message
    subject = "Appointment Confirmation"
    body = f"Dear customer,\n\nWe are pleased to confirm that your appointment has been scheduled for {appointment_date}. Thank you for choosing our business.\n\nSincerely,\nThe Appointment Team"
    message = f"Subject: {subject}\n\n{body}"

    # Send the email
    smtp_server.sendmail("sender@gmail.com", customer_email, message)

    # Close the SMTP server connection
    smtp_server.quit()
