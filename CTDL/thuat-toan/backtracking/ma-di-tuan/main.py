# Nguyễn Ngọc Cường 2321050061
# Mã đi tuần
#giới hạn đệ quy: 1000
import time

# số ô bàn cờ
n = 10

#Khởi tạo bàn cờ
banCo = [[0 for _ in range(n)] for _ in range(n)]
# các bước mã có thể đi
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

print(f'Kích thước {n}x{n}')

startX = int(input(f'Nhập tọa độ y [1-{n}]: ')) -1
startY = int(input(f'Nhập tọa độ x [1-{n}]: ')) -1
if startX >= 0 and startX < n and startY >= 0 and startY < n:
    start = [startY, startX]

count = 0

# đếm số nước đi khả dụng từ vị trí (x, y)
def countMoves(x, y):
    count = 0
    for i in range(8):
        xx = x + moves[i][0]
        yy = y + moves[i][1]
        if 0 <= xx < n and 0 <= yy < n and banCo[xx][yy] == 0:
            count += 1
    return count

def diTuan(x, y):
    global count

    count += 1
    banCo[x][y] = f'0{count}' if count < 10 else f'{count}'
    
    if count >= n**2:
        print("Xong")
        return True
    else:
        # tạo mảng chứa (số cách đi, tọa độ x, tọa độ y)
        next_moves = []
        for i in range(8):
            xx = x + moves[i][0]
            yy = y + moves[i][1]
            if 0 <= xx < n and 0 <= yy < n and banCo[xx][yy] == 0:
                next_moves.append((countMoves(xx, yy), xx, yy))
        
        next_moves.sort()  #tăng dần, ưu tiên chọn số cách đi ít hơn

        for move in next_moves:
            if diTuan(move[1], move[2]):
                return True

        # quay lại nếu kẹt
        count -= 1
        banCo[x][y] = 0
    
    return False

# start
timeStart = time.time()

if diTuan(start[0], start[1]):
    for i in banCo:
        print(i, '\n')
else:
    print("Không tìm được cách đi")

# end
timeEnd = time.time()
runTime = timeEnd - timeStart
print(f"Thời gian chạy: {runTime:.6f} giây")

print('\n\n\n\n\n')
