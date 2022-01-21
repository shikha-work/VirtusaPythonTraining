def check_key(dict_local, skey):
    if skey in dict_local:
        print("Present")
        print("Value = {}".format(dict_local[skey]))
        return

    print("Not Present")
    pass


my_input_dict = {'a':100, 'b':200, 'c': 300}
search_key= input()
check_key(my_input_dict,search_key)