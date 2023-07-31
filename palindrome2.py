check_another = "yes"

while check_another == "yes":
    my_string = input("Enter a string: ")
    my_string_lower = my_string.lower()
    rev_string = ""

    for char in my_string_lower:
        rev_string = char + rev_string
    
    if my_string_lower == rev_string:
        print("Palindrome")
    else:
        print("Not a Palindrome") 

    check_another = input("Enter yes if you want to check another word? ")   

