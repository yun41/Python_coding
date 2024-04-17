s_list = ['abc','bcd','abc','abba','cddc','opq','opq']
new_s_list = []
for n in s_list:
    if n not in new_s_list:
        new_s_list.append(n)

print('s_list =',s_list)
print('new_s_list =',new_s_list)