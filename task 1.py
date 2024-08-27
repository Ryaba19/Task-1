def circular_path(n, m):
    array = list(range(1, n + 1))
    
    path = []
    current_index = 0
    
    for _ in range(n):
        path.append(array[current_index])
        current_index = (current_index + m - 1) % n
    
    
    print("Resulting path:", "".join(map(str, path)))

if __name__ == "__main__":
    while True:
        n = int(input("Enter the value of n: "))
        m = int(input("Enter the value of m: "))
        circular_path(n, m)
        retry = input("Would you like to try again? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Exiting the program. Goodbye!")
            break
