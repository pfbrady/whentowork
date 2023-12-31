from typing import List, Dict, TYPE_CHECKING
from datetime import datetime


class Result:
    def __init__(self, status_code: int, message: str = '', data: List[Dict] = None):
        """
        Result returned from RestAdapter

        :param status_code: HTTP status code
        :param message:
        :param data:
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []


class Employee:
    if TYPE_CHECKING:
        company_id: int
        w2w_employee_id: int
        employee_number: int
        first_name: str
        last_name: str
        primary_phone: int
        secondary_phone: int
        mobile_phone: int
        emails: List[str]
        last_sign_in: datetime
        sign_in_count: int
        primary_address: str
        secondary_address: str
        city: str
        state: str
        zip_code: int
        comments: str
        max_hours_day: int
        max_shifts_days: int
        max_hours_week: int
        max_shifts_week: int
        hire_date: datetime
        status: str
        priority_group: int
        custom_field_1: str
        custom_field_2: str
        biweekly_target_hours: int
        pay_rate: int

    def __init__(self, company_id: int, w2w_employee_id: int, employee_number: int, first_name: str, last_name: str,
                 primary_phone: int, secondary_phone: int, mobile_phone: int, emails: str, last_sign_in: datetime,
                 sign_in_count: int, primary_address: str, secondary_address: str, city: str, state: str, zip_code: int,
                 comments: str, max_hours_day: int, max_shifts_days: int, max_hours_week: int, max_shifts_week: int,
                 hire_date: datetime, status: str, priority_group: int, custom_field_1: str, custom_field_2: str,
                 biweekly_target_hours: int, pay_rate: int):
        """
        Constructor for Employee

        :param company_id: Unique ID for a company
        :param w2w_employee_id: ID for an employee (Unique over employees in W2W system)
        :param employee_number: ID for employee (Unique over employees in the company)
        :param first_name: First name of employee
        :param last_name: Last name of Employee
        :param primary_phone: Primary Phone number of employee
        :param secondary_phone: Secondary Phone number of employee
        :param mobile_phone: Mobile phone number of employee
        :param emails: Email of employee
        :param last_sign_in: Datetime of last sign to W2W in for employee
        :param sign_in_count: Number of times employee has signed in to W2W
        :param primary_address: Street address of employee
        :param secondary_address: Unit/Apt number of employee
        :param city: City of employee’s address
        :param state: State of employee’s address
        :param zip_code: Zip Code of Employee’s address
        :param comments: Comments managers have given to employee
        :param max_hours_day: Maximum allowed hours assigned per day for employee
        :param max_shifts_days: Maximum allowed Shifts assigned per day for employee
        :param max_hours_week: Maximum allowed hours assigned per week for employee
        :param max_shifts_week: Maximum allowed days assigned per week for employee
        :param hire_date: Date employee was hired
        :param status: Custom status icon
        :param priority_group: Priority group employee is a part of when scheduling
        :param custom_field_1: Custom text field 1
        :param custom_field_2: Custom text field 2
        :param biweekly_target_hours: Target hours to be assigned to employee every 2 weeks
        :param pay_rate: Hourly Pay rate for employee
        """
        self.company_id = company_id
        self.w2w_employee_id = w2w_employee_id
        self.employee_number = employee_number
        self.first_name = first_name
        self.last_name = last_name
        self.primary_phone = primary_phone
        self.secondary_phone = secondary_phone
        self.mobile_phone = mobile_phone
        if ',' not in emails:
            self.emails = [emails]
        else:
            self.emails = emails.split(',')
        self.last_sign_in = last_sign_in
        self.sign_in_count = sign_in_count
        self.primary_address = primary_address
        self.secondary_address = secondary_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.comments = comments
        self.max_hours_day = max_hours_day
        self.max_shifts_day = max_shifts_days
        self.max_hours_week = max_hours_week
        self.max_shifts_week = max_shifts_week
        self.hire_date = hire_date
        self.status = status
        self.priority_group = priority_group
        self.custom_field_1 = custom_field_1
        self.custom_field_2 = custom_field_2
        self.biweekly_target_hours = biweekly_target_hours
        self.pay_rate = pay_rate
