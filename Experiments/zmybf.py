def bestFit(n_proc, m_mem, process_sizes, memory_sizes):
    visited = [0] * m_mem
    loc = [-1] * n_proc

    for i in range(n_proc):
        min_diff = float('inf')
        for j in range(m_mem):
            if memory_sizes[j] - process_sizes[i] < min_diff and memory_sizes[j] - process_sizes[i] >=0 and visited[j]==0:
                min_diff = memory_sizes[j]-process_sizes[i]
                loc[i] = j
        if loc[i] != -1:
            visited[loc[i]] = 1
    
    for i in range(n_proc):
        if loc[i] != -1:
            print(f"Process size = {process_sizes[i]} is allocated to memory block {memory_sizes[loc[i]]} and the hole is {memory_sizes[loc[i]]-process_sizes[i]}")
        else:
            print(f"Process size = {process_sizes[i]} is not allocated to any memory loc")



def main():
    n_proc = int(input("Enter the number of processes: "))
    m_mem = int (input("Enter the number of memory blocks: "))

    process_sizes=[]
    mem_sizes=[]

    print("\nEnter the process sizes:")

    for i in range(n_proc):
        psize = int(input(f"Process {i}: "))
        process_sizes.append(psize)


    print("\nEnter the memory block sizes: ")

    for j in range(m_mem):
        msize = int(input(f"Memory block {j}: "))
        mem_sizes.append(msize)

    bestFit(n_proc,m_mem,process_sizes,mem_sizes)


if __name__ == "__main__":
    main()

