import datetime

def set_appointment(customer_name, employee_name, appointment_date):
    """
    Sets an appointment between a customer and an employee on a specified date
    """
    # check if appointment date is valid
    if appointment_date < datetime.date.today():
        print("Invalid appointment date")
        return

    # store appointment details in database
    appointment_details = {
        "customer_name": customer_name,
        "employee_name": employee_name,
        "appointment_date": appointment_date
    }
    # save appointment details to database
    save_to_database(appointment_details)

    # send appointment confirmation email to customer
    email_body = f"Dear {customer_name}, \n\n Your appointment with {employee_name} has been scheduled on {appointment_date}. \n\n Thank you,\n {APP_NAME}"
    send_email(customer_email, email_body)

    # send appointment reminder email to employee
    email_body = f"Dear {employee_name}, \n\n You have an appointment with {customer_name} on {appointment_date}. \n\n Thank you,\n {APP_NAME}"
    send_email(employee_email, email_body)

    # send appointment reminder text message to employee
    text_message = f"Appointment with {customer_name} scheduled on {appointment_date}."
    send_text_message(employee_phone, text_message)

    print("Appointment set successfully")
