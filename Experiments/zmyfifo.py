def get_data():
    global n, in_seq, nf

    n = int(input("Enter the number of pages: "))

    in_seq=[]
    print("Enter the page ref seq: ")
    for _ in range(n):
        in_seq.append(int(input()))
    
    nf  = int(input("Enter the number of page frames: "))


def initialize():
    global pgfaultcount,c,frames
    c=0
    pgfaultcount=0
    frames = [-1]*nf

def fifo():
    initialize()
    for i in range(n):
        page=in_seq[i]
        if page not in frames:
            global pgfaultcount,c
            if -1 in frames:
                empty = frames.index(-1)
                frames[empty] = page
            else:
                frames[c]=page
                c=(c+1)%nf
            pgfaultcount += 1

        for frame in frames:
            print(frame, end=' ')
        print()

if __name__ == "__main__":
    get_data()
    fifo()
    print("Page fault count = ",pgfaultcount)