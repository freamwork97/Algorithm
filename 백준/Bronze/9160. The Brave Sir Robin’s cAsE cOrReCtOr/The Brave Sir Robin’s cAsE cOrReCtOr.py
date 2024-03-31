import re
import sys

new = ""

a = sys.stdin.readlines()
# print(a)
flag_cap = False
for i in range(len(a)):
    a[i] = a[i].lower()
    # print(a[i][:])

    if flag_cap == True:
        a[i] = a[i].capitalize()
        # print(a[i])
        new += re.sub(
            # r"([.!?)(])(\s)(\w)|([.!?)(])(\w)|((\\n)[.!?)(])(\s)(\w)|((\\n)[.!?)(])(\w)",
            r"([.!?()]\s*(\w)|[.!?()](\w))",
            lambda n: n.group().upper(),
            a[i],
        )
        flag_cap = False
    else:
        new += re.sub(
            r"([.!?()]\s*(\w)|[.!?()](\w))",
            lambda n: n.group().upper(),
            a[i],
        )
        if re.search(r"[.!?()](\n)", a[i]):
            flag_cap = True
        else:
            flag_cap = False


new = new.replace("\n", " ")
print(new)