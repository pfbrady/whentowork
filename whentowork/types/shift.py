from typing import Optional, TypedDict


class Shift(TypedDict):
    """
    Type Format for Shift

    :param COMPANY_ID:
    :param SHIFT_ID:
    :param PUBLISHED:
    :param W2W_EMPLOYEE_ID:
    :param FIRST_NAME:
    :param LAST_NAME:
    :param EMPLOYEE_NUMBER:
    :param START_DATE:
    :param START_TIME:
    :param END_DATE:
    :param END_TIME:
    :param DURATION:
    :param DESCRIPTION:
    :param POSITION_ID:
    :param POSITION_NAME:
    :param CATEGORY_ID:
    :param CATEGORY_NAME:
    :param CATEGORY_SHORT:
    :param COLOR_ID:
    :param PAY_RATE:
    :param POSITION_CUSTOM1:
    :param POSITION_CUSTOM2:
    :param POSITION_CUSTOM3:
    :param CATEGORY_CUSTOM1:
    :param CATEGORY_CUSTOM2:
    :param CATEGORY_CUSTOM3:
    :param LAST_CHANGED_TS:
    :param LAST_CHANGED_BY:
    """
    COMPANY_ID: int
    SHIFT_ID: int
    PUBLISHED: str
    W2W_EMPLOYEE_ID: int
    FIRST_NAME: str
    LAST_NAME: str
    EMPLOYEE_NUMBER: int
    START_DATE: str
    START_TIME: str
    END_DATE: str
    END_TIME: str
    DURATION: int
    DESCRIPTION: str
    POSITION_ID: int
    POSITION_NAME: str
    CATEGORY_ID: Optional[int]
    CATEGORY_NAME: Optional[str]
    CATEGORY_SHORT: Optional[str]
    COLOR_ID: int
    PAY_RATE: Optional[int]
    POSITION_CUSTOM1: str
    POSITION_CUSTOM2: str
    POSITION_CUSTOM3: str
    CATEGORY_CUSTOM1: Optional[str]
    CATEGORY_CUSTOM2: Optional[str]
    CATEGORY_CUSTOM3: Optional[str]
    LAST_CHANGED_TS: str
    LAST_CHANGED_BY: str
