def bin_to_dec():
    x = input()
    base = 1
    final_list = []
    for bin in x.split(","):
        print(bin)
        num = 0
        for i in range(len(bin)-1,-1,-1):
            print(bin[i])
            if int(bin[i]) == base:
                num += 2**(len(bin)-1-i)
                print("encountered One")
                print(num)
            else:
                print("encountered zero")
        print("final num = {}".format(num))
        if num % 5 == 0:
            final_list.append(num)
    print(final_list)


bin_to_dec()