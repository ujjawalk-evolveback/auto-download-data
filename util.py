from datetime import date
from dateutil.relativedelta import relativedelta

''' This file generates a dictinary of months which contains
    start and end date of each months. '''

def last_date_of_month(d: date) -> date:
    return (date(d.year + d.month//12, d.month%12+1, 1) - relativedelta(days=1))

def get_months_dict():
    today = date.today()
    last_date = last_date_of_month(today)
    months_dict = {}
    months_dict[0] = [today.strftime("%Y/%m/%d"), last_date.strftime("%Y/%m/%d")]

    for i in range(1, 12):
        start_date = last_date + relativedelta(days=+1)
        end_date = start_date + relativedelta(months=+1) + relativedelta(days=-1)
        months_dict[i] = [start_date.strftime("%Y/%m/%d"), end_date.strftime("%Y/%m/%d")]
        last_date = end_date

    return months_dict