my_dict = {}
while True:
    input(my_dict)
    print("Do you want to add/modify the dictionary?")
    inp = input()
    if "ADD" or "MODIFY"  in inp.upper():
        k = input()
        v = int(input())
        my_dict[k] = v
