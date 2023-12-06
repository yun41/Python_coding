# str1 = '아버지:어머니:오빠:형'
# str2 = str1.split(':')
# str3 = "/".join(str2)
# print(str3)

# str1 = '아버지:어머니:오빠:형'
# str2 = str1.replace(":","/")
# print(str2)

str1 = ' bigdata have a good future prospect'
str2 = str1.lstrip()
print(str2)
for i in str2:
    if i.isupper() == False:
        str3 = str2.upper()
print(str3)