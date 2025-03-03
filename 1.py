from datetime import datetime
import re

def get_days_from_today(date:str) -> int:
    if isinstance(date, str) and re.fullmatch(r'\d{4}-(\d{1}|\d{2})-\d{2}', date) is not None: 
        datetime_obj = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        num_of_days = today.toordinal() - datetime_obj.toordinal() 
        return num_of_days


#additional

# audit
print(get_days_from_today("2025-3-04"))

# asserts for 2025-3-03
# assert get_days_from_today("2025-3-04") == -1
# assert get_days_from_today("2025-3-03") == 0
# assert get_days_from_today("2025-3-02") == 1
# assert get_days_from_today("2000-2-11") == 9152
# assert get_days_from_today("2021-10-09") == 1241
assert get_days_from_today("assa") == None
assert get_days_from_today(True) == None
