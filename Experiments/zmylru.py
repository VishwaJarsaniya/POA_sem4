np = int(input("Enter the number of pages: "))
nf = int(input("Enter the number of frames: "))

pages = [0]*np
frames = [-1]*nf
c2 = [0]*nf
global pgfaultcount 
global k 

for i in range (np):
    pages[i] = int(input(f"Enter the {i+1}th page: "))

def optimal():
    pgfaultcount = 0
    k = 0
    for i in range(np):
        c1=0
        for j in range(nf):
            if frames[j]!=pages[i]:
                c1+=1
            else:
                break
        if (c1==nf):
            if k<nf:
                frames[k]=pages[i]
                k+=1
                pgfaultcount+=1
            else:
                ##lru pg replacement
                for r in range(nf):
                    c2[r]=0
                    for p in range(i-1,-1,-1):
                        if frames[r]!=pages[p]:
                            c2[r]+=1
                        else:
                            break
        
                b = c2[:]

                b.sort(reverse=True)

                for r in range(nf):
                    if c2[r]==b[0]:
                        frames[r]=pages[i]
                        pgfaultcount+=1
                        break
        print(frames)

    print("Page fault count = ",pgfaultcount)


if __name__ == "__main__":
    optimal()
        




                            