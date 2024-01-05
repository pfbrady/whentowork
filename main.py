from datetime import date
from whentowork.client import Client
from settings import W2W_TOKEN

a = Client(hostname='www3.whentowork.com/cgi-bin/w2wC4.dll', api_key=W2W_TOKEN)
print(a.get_employee_by_id(564685546).first_name)
print(a.get_shifts_by_date(date(2023, 12, 18), date(2023, 12, 18)))
