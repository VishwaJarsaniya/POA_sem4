def get_data():
    global n, in_seq, nf
    n = int(input("Enter the length of the page reference sequence: "))
    
    in_seq = []
    print("Enter the page reference sequence: ")
    for _ in range(n):
        in_seq.append(int(input()))
    
    nf = int(input("Enter the number of frames: "))

def initialize():
    global pgfaultcount, frames, c
    pgfaultcount = 0
    frames = [-1] * nf
    c = 0

def fifo():
    initialize()
    for i in range(n):
        page = in_seq[i]
        if page not in frames:
            global pgfaultcount, c
            if -1 in frames:
                empty_index = frames.index(-1)
                frames[empty_index] = page
            else:
                frames[c] = page
                c = (c + 1) % nf
            pgfaultcount += 1
        
        # Display pages
        for frame in frames:
            print(frame, end=' ')
        print()

if __name__ == "__main__":
    get_data()
    fifo()
    print("Page fault count:", pgfaultcount)
