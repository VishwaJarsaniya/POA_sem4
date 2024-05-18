def firstFit(n_proc, m_mem, process_sizes, mem_sizes):
    visited = [0]*m_mem
    loc = [-1]*n_proc

    for i in range(n_proc):
        for j in range(m_mem):
            if mem_sizes[j] > process_sizes[i] and visited[j]==0:
                loc[i] = j
                break
        if loc[i]!=-1:
            visited[loc[i]] = 1
    
    for i in range(n_proc):
        if loc[i]!=-1:
            print(f"Process {i} (psize = {process_sizes[i]}) is allocated to memory block {loc[i]} (msize = {mem_sizes[loc[i]]})")
        else:
            print(f"Process {i} (psize = {process_sizes[i]}) is NA")
            

def main():
    process_sizes = []
    mem_sizes = []

    n_proc = int(input("Enter the number of processes: "))
    m_mem = int(input("Enter the number of memory blocks: "))
    print("\nEnter the process sizes:")
    for i in range (n_proc):
        psize = int(input(f"Process {i}: "))
        process_sizes.append(psize)
    print("\nEnter the block sizes:")
    for j in range (m_mem):
        msize = int(input(f"Memory block {j+1}: "))
        mem_sizes.append(msize)
    
    firstFit(n_proc,m_mem,process_sizes,mem_sizes)

if __name__ == "__main__":
    main()