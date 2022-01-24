input_letter  = input("Enter a character  to be checked:\n ")

vowels = [ 'A','E','I','O','U','a','e','i','o','u' ]


if input_letter in vowels:
    print(input_letter, "is a vowel")
else:
    print(input_letter, "is a consonent")
