def Sort_0_Right(arr):
    c =arr.count(0)
    new_arr = [i for i in arr if i!=0]+[0]*c
    print(new_arr)
arr = [-1,10,0,0,0,10,20,30,0,0,0]
Sort_0_Right(arr)

# todo The same code for left sorting/pushing of 0

# def Sort_0_Right(arr):
    # c =arr.count(0)
    # new_arr = [0]*c + [i for i in arr if i!=0]
    # print(new_arr)
# arr = [-1,10,0,0,0,10,20,30,0,0,0]
# Sort_0_Right(arr)