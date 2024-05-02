# string = input("Enter a string: ")
#
# vowels = "aeiouAEIOU"
# vow_count = 0
# cons_count = 0
#
# for i in string:
#     if i in vowels:
#         vow_count += 1
#     else:
#         cons_count += 1
#
# print(cons_count)
# print(vow_count)


def vowelsCount(string):
    vowels = "aeiouAEIOU"
    vow_count = 0
    for i in string:
        if i in vowels:
            vow_count += 1
    return vow_count


output = vowelsCount("iam a QAEngineer")
print(output)
