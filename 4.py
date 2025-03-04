from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    users_to_congr = []
    today = datetime.today().date()
    for user in users:
        date_of_birth= datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        if today < date_of_birth: continue

        birthday_this_year = date_of_birth.replace(year=today.year)
        next_bd = date_of_birth.replace(year=today.year + 1) if birthday_this_year < today else birthday_this_year  
        
        if next_bd.toordinal() - today.toordinal() <= 7:    
            bday_of_week = next_bd.weekday()
            if bday_of_week == 5:
                next_bd = next_bd + timedelta(days = 2)
            if bday_of_week == 6:
                next_bd = next_bd + timedelta(days = 1)
        
            congratulation_date = next_bd.strftime("%Y.%m.%d")
            users_to_congr.append({"name":user["name"], "congratulation_date":congratulation_date})

    return users_to_congr


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "James T. Kirk", "birthday": "2024.03.05"},
    {"name": "Sarah Connor", "birthday": "1970.03.08"},
    #parameters aren't correct
    {"name": "Spock", "birthday": "2027.10.10"},
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)