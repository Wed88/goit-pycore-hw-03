from datetime import datetime

def get_days_from_today(date):

    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        today_date = datetime.today().date()
        
        delta = today_date - target_date
        
        return delta.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."

# print(get_days_from_today("2021-10-09")) 
# print(get_days_from_today("2025-10-09")) 
# print(get_days_from_today("неправильна дата"))
