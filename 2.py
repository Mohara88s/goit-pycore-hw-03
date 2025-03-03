from typing import List
import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> List[int]:
    list_of_num=[]
    if min>=1 and max<=1000 and max>=quantity and quantity>=min:
        while len(list_of_num) < quantity:
            num = random.randint(min, max)
            if not num in list_of_num: 
                list_of_num.append(num)
        list_of_num.sort()
    return list_of_num
    

#additional

# audit
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1,100,20)
print("Ваші лотерейні числа:", lottery_numbers)

#parameters aren't correct
lottery_numbers = get_numbers_ticket(1,100,200) 
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(100,100,20) 
print("Ваші лотерейні числа:", lottery_numbers)
