croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input_string=input()
for alphabet in croatian_alphabets:
    input_string = input_string.replace(alphabet, '*')
print(len(input_string))
