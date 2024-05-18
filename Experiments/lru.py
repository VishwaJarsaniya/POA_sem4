def get_data():
    global n, in_seq, nf
    n = int(input("Enter the length of the page reference sequence: "))
    
    in_seq = []
    print("Enter the page reference sequence: ")
    for _ in range(n):
        in_seq.append(int(input()))
    
    nf = int(input("Enter the number of frames: "))

def initialize():
    global frames
    frames = [-1] * nf

def lru():
    global pgfaultcount
    initialize()
    pgfaultcount = 0
    c2 = [0] * nf  # Counter for the LRU algorithm

    for i in range(n):
        page = in_seq[i]
        if page in frames:
            contin # Page is already in frames, no fault
        
        # Page fault occurred
        if -1 in frames:
            # There is still space in the frames
            empty_index = frames.index(-1)
            frames[empty_index] = page
        else:
            # Apply LRU algorithm
            for r in range(nf):
                c2[r] = 0
                for j in range(i - 1, -1, -1):
                    if frames[r] != in_seq[j]:
                        c2[r] += 1
                    else:
                        break
            
            # Copy in b
            b = c2[:]
            
            # Ascending bubble sort
            for a in range(nf):
                for d in range(a, nf):
                    if b[a] < b[d]:
                        b[a], b[d] = b[d], b[a]
            
            for r in range(nf):
                if c2[r] == b[0]:
                    frames[r] = page
                    break
        
        pgfaultcount += 1

        # Display the frames
        for frame in frames:
            print(frame, end=' ')
        print()
    
    print("Page fault count:", pgfaultcount)

if __name__ == "__main__":
    get_data()
    lru()
