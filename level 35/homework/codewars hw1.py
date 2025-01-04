def even_numbers(arr,n):
    even_list = []
    for i in arr:
        if i % 2 == 0:
            even_list.append(i)
    return even_list[-n:]