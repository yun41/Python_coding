storage = []
map_ = []

for _ in range(5):
    map_list = list(map(str, input().split()))
    map_.append(map_list)

print(map_)
storage.append(map_[0:1][0:2])
storage.append(map_[1:2][0:2])
print(storage)

result = 0
for i in range(len(storage)):
    result += sum(storage[i])
print(result)