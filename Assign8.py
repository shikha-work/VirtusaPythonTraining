def find_case(str1):
    count_upper = 0
    count_lower = 0
    for i in str1:
        if i.isupper():
            count_upper+=1
        elif i.islower():
            count_lower+=1

    print(count_upper)
    print(count_lower)


string1 = input()
find_case(string1)
