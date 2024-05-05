str = input()
# result = ""
result2 = [
    str[i].lower() if str[i].isupper() else str[i].upper() for i in range(len(str))
]
# for i in range(len(str)):
#     result += str[i].lower() if str[i].isupper() else str[i].upper()
# if str[i].isupper():
#     result += str[i].lower()
# elif str[i].islower():
#     result += str[i].upper()
for i in result2:
    print(i, end="")
