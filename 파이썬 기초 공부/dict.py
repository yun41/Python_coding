dict1 = {1:"man", 2:"woman",3:"baby"}
print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict2 = {4:100, 5:200, 6:300, 7:400}
dict1.update(dict2)
dict2.clear

names = {'오현민':10999, '이주경':2111, '권도훈':9778, '김아영':20245, '박서혜':27115,'안준한':5887, '박수정':7855}
names['오현민']=30000
del names['이주경']
print(names.items())
print(names.keys())
print(names.values())