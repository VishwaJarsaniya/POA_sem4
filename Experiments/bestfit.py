def best_fit(n_proc, n_mem, mem_sizes, process_sizes):
    mem_loc = [-1] * n_proc
    visited = [0] * n_mem

    for i in range(n_proc):
        min_diff = float('inf')
        for j in range(n_mem):
            if mem_sizes[j] - process_sizes[i] < min_diff and mem_sizes[j] - process_sizes[i] >= 0 and visited[j] == 0:
                min_diff = mem_sizes[j] - process_sizes[i]
                mem_loc[i] = j
        if mem_loc[i] != -1:
            visited[mem_loc[i]] = 1

    for i in range(n_proc):
        if mem_loc[i] != -1:
            print(f"Process size = {process_sizes[i]} goes in location {mem_sizes[mem_loc[i]]} and hole is {mem_sizes[mem_loc[i]] - process_sizes[i]}")
        else:
            print(f"{process_sizes[i]} not allocated to memory")


def main():
    n_proc = int(input("Enter the number of processes: "))
    n_mem = int(input("Enter the number of memory blocks: "))

    mem_sizes = []
    process_sizes = []

    # Input memory sizes
    print("Enter the sizes of memory blocks:")
    for i in range(n_mem):
        size = int(input(f"Memory block {i + 1}: "))
        mem_sizes.append(size)

    # Input process sizes
    print("Enter the sizes of processes:")
    for i in range(n_proc):
        size = int(input(f"Process {i + 1}: "))
        process_sizes.append(size)

    # Call Best Fit algorithm function
    best_fit(n_proc, n_mem, mem_sizes, process_sizes)


if __name__ == "__main__":
    main()
