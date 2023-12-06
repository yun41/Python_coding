N = int(input())

for i in range(1, N+1):
    if i <= 10:
        if i % 3 == 0:
            print("-", end=' ')
        else:
            print(i, end=' ')

    elif i <= 100:
        if i == 30 or i == 60 or i == 90:
            print("-", end=' ')
        # 십의 자리 수가 3,6,9일 때
        elif (i//10)%3==0:
            # 일의 자리 수가 3,6,9일 때
            if (i%10)%3 == 0:
                print("--", end=' ')
            else:
                print("-", end=' ')

        # 십의 자리 수가 3,6,9가 아닐 때
        elif i%10 == 0:
            print(i, end=' ')
        elif (i%10)%3 == 0:
                print("-", end=' ')
        else:
            print(i, end=' ')

    elif i <= 1000:
        if i == 300 or i == 600 or i == 900:
            print("-", end=' ')
        # 백의 자리 수가 3,6,9 일 때
        elif(i//100)%3==0:
            if (i%100) == 30 or (i%100) == 60 or (i%100) == 90:
                print("--", end = ' ')
            # 십의 자리 수가 3,6,9 일 때
            elif((i%100)//10)%3==0:
                # 일의 자리 수가 3,6,9 일 때
                if((i%100)%10)%3==0:
                    print("---", end=' ')
                else:
                    print("--", end=' ')

            # 십의 자리 수가 3,6,9가 아닐 때
            elif (i%100)%10 == 0:
                print("-", end=' ')
            # 일의 자리 수가 3,6,9 일 때
            elif((i%100)%10)%3==0:
                print("--", end=' ')
            # 일의 자리 수가 3,6,9가 아닐 때
            else:
                 print("-", end=' ')

        # 백의 자리 수가 3,6,9가 아닐 때
        elif i%100==0:
            print(i, end=' ')
        # 십의 자리 수가 3,6,9일 때
        elif((i%100)//10)%3==0:
            # 일의 자리 수가 3,6,9일 때
            if((i%100)%10)%3==0:
                print("--", end=' ')
            else:
                print("-", end=' ')
        # 십의 자리 수가 3,6,9가 아닐 때
        elif (i%100)%10 == 0:
            print(i, end=' ')
        elif((i%100)%10)%3==0:
            print("-", end=' ')
        else:
            print(i, end=' ')