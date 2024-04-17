string_given = 'Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)'
count_string = string_given.count('Bython')
string_changed = string_given.replace('Bython','Python')
print(string_changed)
print('Bython 문자열은 모두 {}번 수정했습니다.'.format(count_string))