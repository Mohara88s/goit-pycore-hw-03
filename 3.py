import re

def normalize_phone(phone_number:str)->str:
    pattern = r"[^+\d]"
    replacement = ""
    cleared_phone = re.sub(pattern, replacement, phone_number)
    if len(cleared_phone) and cleared_phone[0]=='+':
        normalized_phone=cleared_phone
    elif len(cleared_phone) and cleared_phone[0]=='3':
        normalized_phone = '+' + cleared_phone
    elif len(cleared_phone) and cleared_phone[0]=='8':
        normalized_phone = '+3' + cleared_phone
    elif len(cleared_phone) and cleared_phone[0]=='0':
        normalized_phone = '+38' + cleared_phone
    else:
        return
    if len(normalized_phone)!=13: return
    return normalized_phone


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    #parameters aren't correct
    "18050 111 22 11   ",
    "assa   ",
    "38050 111 22    ",
    "38050 111 22 11 00  ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

