
import re
card_no = "1111-2222-3333-444" 
card = card_no.split("-")
new_card = ''.join(card)
group = list(set([len(i) for i in card]))

valid = False

if len(new_card) == 16 and len(re.findall("\d",new_card)) == 16 and group[0] == 4: 
    if re.findall("\A3", card_no) or re.findall("\A4", card_no) or re.findall("\A9", card_no): 
        valid = True
        
c=0
if valid == True:  
    for i in range(len(new_card) - 2):
        if new_card[i] == new_card[i + 1] and new_card[i + 1] == new_card[i + 2]:
            c+=1
            if c == 1:
                valid = False
                break

                
if valid == True:
    print("Credit Card is a Valid card")
else:
    print("Credit Card is not Valid card")
