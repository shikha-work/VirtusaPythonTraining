def create_matrix():
    i = int(input())
    j = int(input())
    list_main = []
    list_tmp = []
    for x in range(i):
        list_tmp = []
        for y in range(j):
            list_tmp.append(x*y)
        list_main.append(list_tmp)
    print(list_main)

create_matrix()