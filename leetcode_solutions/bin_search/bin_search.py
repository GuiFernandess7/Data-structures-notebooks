def findTargetPair(A: list, left, right): # FAILED
    st = set()
    bigger_value_position = A.index(max(A))
    for i in range(len(A)):
        pass
    return bigger_value_position

def bin_search(A, left, right):
    bigger_value = 0
    group_set_divider = 1
    hash_m = {}

    while group_set_divider < len(A):
        sum_value = sum(A)

        if bigger_value < sum_value:
            bigger_value = sum_value
            hash_m[group_set_divider] = bigger_value
        else:
            A = A[:len(A) // group_set_divider]

        group_set_divider += 1

    return hash_m

#original_lista = [-2, 1 , -3 , 4 , -1 , 2 , 1 , -5 , 4]
#print(bin_search(original_lista, 0, len(original_lista)))

#sublistas = [original_lista[i:i + 3] for i in range(0, len(original_lista), 3)]
#print(sublistas)
#A = original_lista[len(original_lista) // 3:]
#print(A)

