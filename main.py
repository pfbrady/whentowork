from datetime import date
from whentowork.client import Client
from settings import W2W_TOKEN, W2W_HOSTNAME

a = Client(hostname=W2W_HOSTNAME, api_key=W2W_TOKEN)
print(a.get_employee_by_id(564685546).first_name)
print(a.get_shifts_by_date(date(2023, 12, 18), date(2023, 12, 18)))
b = a.get_timeoff_by_date(date(2023, 12, 18), date(2023, 12, 18))
print(b[0].employee)
