from collections import Counter

arr = [10, 2, 3, 4, 3, 9, 3, 10]

def get_most_recurrent_char(arr):
    ocrr = Counter(arr).most_common()
    return ocrr[0][0]

def get_most_recurrent_char2(arr):
    hash_m = {}
    occ = 1

    for i in arr:
        if i in hash_m:
            occ += 1
        hash_m[i] = occ

    occs = max(hash_m, key=lambda k: hash_m[k])
    return occs

def get_most_recurrent_char3(arr):
    hash_m = {}

    for idx, char in enumerate(arr):
        if char in hash_m:
            return char
        hash_m[char] = idx

print(get_most_recurrent_char3(arr))