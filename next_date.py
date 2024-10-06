from datetime import datetime, timedelta

def next_date (date_str):
    date_format = "%d/%m/%Y"
    date = datetime.strptime(date_str, date_format)
    next_date = date + timedelta(days=1)
    return next_date.strftime(date_format)

# Test the function
s = input()
print(next_date(s))
