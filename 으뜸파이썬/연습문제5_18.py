s_list = ['abc','bcd','bcdefg','abba','cddc','opq']
s_list_len = []
for i in range(len(s_list)):
    s_list_len.append(len(s_list[i]))

s_list_len_1 = s_list_len.copy()

min_num = 9999
for l in range(len(s_list_len)-1):
    if s_list_len[l] < min_num:
        min_num = s_list_len[l]

max_num = 0
for k in range(len(s_list_len_1)):
    if s_list_len_1[k] > max_num:
        max_num = s_list_len_1[k]

loc_num = s_list_len.index(min_num)
print('가장 길이가 짧은 문자열 :',s_list[loc_num])

loc_num_1 = s_list_len_1.index(max_num)
print('가장 길이가 긴 문자열 :',s_list[loc_num_1])

s_list.sort(key=len)
print('가장 길이가 짧은 문자열 :',end=' ')
for m in range(len(s_list)):
    if len(s_list[m]) == len(s_list[0]):
        print(f'{s_list[m]}',end=' ')