"""
Upper and Lower
"""
# Provide your solution here

def count_upper_lower(word: str):
    list_upper = []
    list_lower = []

    for letters in word:
        if letters.isupper():
            list_upper.append(letters)
        else:
            list_lower.append(letters)
    # print(list_upper)
    print("No. of Upper case characters: ", len(list_upper))
    # print(list_lower)
    print("No. of Lower case characters: ", len(list_lower))



my_word = "aAbBc"
count_upper_lower(my_word)




"""
Check 33
"""
# Provide your solution here

def has_33(list: [int]) -> bool:
    for i in list:
        if (33 in list):
            return True
        else:
            return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

a = has_33([1, 2, 3, 13, 33, 100])
print(a)
b = has_33([4, 58, 6, 12])
print(b)
c = has_33([10, 12, 3, 48, 13, 33])
print(c)
