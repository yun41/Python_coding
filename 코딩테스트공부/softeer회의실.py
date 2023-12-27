import sys
input = sys.stdin.readline

N, M = map(int, input().split())
room_name = [0] * N
reserv_info = [0] * M

for i in range(N):
    room_name[i] = input().rstrip()

for j in range(M):
    reserv_info[j] = list(map(str, input().split()))

room_name.sort()
for room_name_index in range(N):
    timeline = ['09-10','10-11','11-12','12-13','13-14','14-15','15-16','16-17','17-18']
    time_blank = ['9','10','11','12','13','14','15','16','17','18']
    result = []
    count = 1
    
    for reserv_info_index in range(M):
        if room_name[room_name_index] == reserv_info[reserv_info_index][0]:
            index_len = int(reserv_info[reserv_info_index][2]) - int(reserv_info[reserv_info_index][1])
            start = time_blank.index(reserv_info[reserv_info_index][1])
            del timeline[start:start + index_len]
            del time_blank[start:start + index_len]
    
    print(f'Room {room_name[room_name_index]}:')
    if len(timeline) == 0:
        print('Not available')
    else:
        for x in range(len(timeline)-1):
            if timeline[x][3:] != timeline[x+1][:2]:
                result.append(x)
                count += 1
        result.append(len(timeline)-1)
        print(count,'available:')

        for y in range(count):
            if y > 0:
                print(f'{timeline[result[y-1]+1][:3]}{timeline[result[y]][3:]}')
            else:
                print(f'{timeline[0][:3]}{timeline[result[y]][3:]}')

    if room_name_index != N - 1:
        print('-----')
    
