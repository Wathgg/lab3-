from collections import deque

def min_knight_moves(start, end):
    directions = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2),
    ]
    
    visited = [[False for _ in range(8)] for _ in range(8)]
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited[start[0]-1][start[1]-1] = True
    
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == (end[0], end[1]):
            return dist
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 1 <= nx <= 8 and 1 <= ny <= 8:
                if not visited[nx-1][ny-1]:
                    visited[nx-1][ny-1] = True
                    queue.append((nx, ny, dist + 1))
    
    return -1

def read_coordinate(prompt):
    while True:
        try:
            input_str = input(prompt)
            parts = input_str.strip().split()
            if len(parts) != 2:
                print("Введите две координаты через пробел, например: 1 1")
                continue
                
            x, y = map(int, parts)
            
            if not (1 <= x <= 8 and 1 <= y <= 8):
                print("Координаты должны быть в диапазоне от 1 до 8.")
                continue
                
            return (x, y)
        except ValueError:
            print("Координаты должны быть числами. Попробуйте снова.")

def main():
    print("Введите координаты клеток шахматной доски (числа от 1 до 8).")
    
    start = read_coordinate("Начальная позиция (x y): ")
    end = read_coordinate("Конечная позиция (x y): ")
    
    moves = min_knight_moves(start, end)
    if moves >= 0:
        print(f"Минимальное количество ходов коня: {moves}")
    else:
        print("Путь не найден (что маловероятно на стандартной доске).")

if __name__ == "__main__":
    main()