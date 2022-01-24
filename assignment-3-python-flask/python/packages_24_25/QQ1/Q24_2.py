from QQ1.Q24_1 import checkPalindrome, reverseStr, evenOdd

import random

ran = random.randint(1,1000)
print("Random number from 1 to 1000 is \n" , ran )

ans1 = checkPalindrome("kadam")
ans2= reverseStr("quantiphi")
ans3= evenOdd(9)

print("Palindrone of string is ",ans1)
print("Reverse of string is",ans2)
print("Even Odd check",ans3)