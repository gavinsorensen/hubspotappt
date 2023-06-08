# Import necessary modules for integration with Hubspot App's calendar
import hubspot
import calendar

# Define function to check availability of dates and times in Hubspot App's calendar
def check_availability(start_time, end_time):
    # Use Hubspot API to retrieve calendar data and check for conflicting events
    calendar_data = hubspot.get_calendar_data()
    for event in calendar_data:
        if start_time >= event['start_time'] and start_time <= event['end_time']:
            return False
        elif end_time >= event['start_time'] and end_time <= event['end_time']:
            return False
    return True

# Define function to set appointment and add it to Hubspot App's calendar
def set_appointment(customer_name, customer_email, employee_name, start_time, end_time):
    # Check for availability of selected dates and times
    if check_availability(start_time, end_time):
        # Use Hubspot API to create appointment event and add it to calendar
        appointment_data = {
            'customer_name': customer_name,
            'customer_email': customer_email,
            'employee_name': employee_name,
            'start_time': start_time,
            'end_time': end_time
        }
        hubspot.create_appointment_event(appointment_data)
        return True
    else:
        return False
