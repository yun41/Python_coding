import sys
input = sys.stdin.readline
N, M = map(int, input().split())
m_ms_ = []
reality_m_ms_ = []
velo = []
total = 100
i=0
j=0

def velocity_(x,y):
    if m_ms_[x][1] < reality_m_ms_[y][1]:
        velo.append(reality_m_ms_[y][1] - m_ms_[x][1])
    else:
        velo.append(0)
    
    return velo

for _ in range(N):
    m_ms = list(map(int, input().split()))
    m_ms_.append(m_ms)

for _ in range(M):
    reality_m_ms = list(map(int, input().split()))
    reality_m_ms_.append(reality_m_ms)

while total != 0:
    if m_ms_[i][0] > reality_m_ms_[j][0]:
        velocity_(i,j)
        total -= reality_m_ms_[j][0]
        m_ms_[i][0] -= reality_m_ms_[j][0]
        j += 1
    elif m_ms_[i][0] == reality_m_ms_[j][0]:
        velocity_(i,j)
        total -= reality_m_ms_[j][0]
        i += 1
        j += 1
    else:
        velocity_(i,j)
        total -= m_ms_[i][0]
        reality_m_ms_[j][0] -= m_ms_[i][0]
        i += 1

print(max(velo))