import re
s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'

s1_1=s1.replace(" ","")
s1_1=s1_1.replace("-","")
s2_1=s2.replace(" ","")
s2_1=s2_1.replace("-","")
s3_1=s3.replace(" ","")
s3_1=s3_1.replace("-","")
s4_1=s4.replace(" ","")
s4_1=s4_1.replace("-","")
s1_1=s1_1.upper()
s2_1=s2_1.upper()
s3_1=s3_1.upper()
s4_1=s4_1.upper()

print("{}(은)는 {}(으)로 수정됨".format(s1,s1_1))
print("{}(은)는 {}(으)로 수정됨".format(s2,s2_1))
print("{}(은)는 {}(으)로 수정됨".format(s3,s3_1))
print("{}(은)는 {}(으)로 수정됨".format(s4,s4_1))
print("{} : {}개의 N이 나타남".format(s1_1,s1_1.count('N')))
print("{} : {}개의 N이 나타남".format(s2_1,s2_1.count('N')))
print("{} : {}개의 N이 나타남".format(s3_1,s3_1.count('N')))
print("{} : {}개의 N이 나타남".format(s4_1,s4_1.count('N')))