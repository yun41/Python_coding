def cel2fah(cel):
    return (9/5)*cel+32

for i in range(10,60,10):
    print(f'섭씨 {i} 도 = 화씨 {cel2fah(i)} 도')