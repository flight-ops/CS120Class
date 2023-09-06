end_message = "Thank you. Here is your pay."
prompt_user_for_hours_worked = float(input("How many hours did you work?"))
prompt_user_for_hourly_pay = float(input("What is your hourly wage?"))
print(end_message)
print(prompt_user_for_hours_worked * prompt_user_for_hourly_pay)
