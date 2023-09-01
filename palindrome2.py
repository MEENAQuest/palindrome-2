check="y"
while check=="y":
    my_string = input("Enter a string: ")
    my_string_lower = my_string.lower()
    len_string = len(my_string_lower)

    i=0
    j=len_string - 1

    for i in range(len_string):
        if my_string_lower[i] == my_string_lower[j]:
            i=i+1
            j=j-1
            flag=1
        else:
            flag=0
            break

    if flag==1:
        print("Palindrome")
    if flag==0:
        print("Not a Palindrome")

    check = input("Enter y if you want to check another word? ")       
