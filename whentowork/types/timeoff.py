from typing import Optional, TypedDict


class TimeOff(TypedDict):
    """
    Type Format for TimeOff

    :param COMPANY_ID: Unique ID for a company
    :param TIMEOFF_ID: Unique ID for a Time Off Reservation
    :param W2W_EMPLOYEE_ID: ID for an employee (Unique over employees in W2W system)
    :param FIRST_NAME: First name of employee
    :param LAST_NAME: Last name of Employee
    :param EMPLOYEE_NUMBER: ID for employee (Unique over employees in the company)
    :param DESCRIPTION: Description of time off
    :param PARTIAL_DAY: Y if partial day off N if full day off
    :param START_DATE:
    :param START_TIME:
    :param END_DATE:
    :param END_TIME:
    :param WHEN_REQUESTED_TS:
    :param LAST_CHANGED_TS:
    :param LAST_CHANGED_BY:
    """
    COMPANY_ID: int
    TIMEOFF_ID: int
    W2W_EMPLOYEE_ID: int
    FIRST_NAME: str
    LAST_NAME: str
    EMPLOYEE_NUMBER: int
    DESCRIPTION: str
    PARTIAL_DAY: str
    START_DATE: str
    START_TIME: str
    END_DATE: str
    END_TIME: str
    WHEN_REQUESTED_TS: str
    LAST_CHANGED_TS: str
    LAST_CHANGED_BY: str
