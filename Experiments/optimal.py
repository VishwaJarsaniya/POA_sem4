np=int(input("enter the number of pages"))
nf=int(input("enter the number of frames"))

pages=[0]*np
frames=[-1]*nf
c2=[0]*nf
faults=k=index=0

for i in range(0,np):
    pages[i]=int(input(f"enter the {i}th page "))

for i in range(0,np):
    c1=0
    for j in range(0,nf):
        if frames[j]!=pages[i]:
            c1+=1
        else:
            break
    if(c1==nf):
        if k<nf:
            frames[k]=pages[i]
            k+=1
            faults+=1
        else:
            for r in range(0,nf):
                c2[r]=0
                for p in range(i,np):
                    if frames[r]!=pages[p]:
                        c2[r]+=1
                    else:
                        break
                
            b=c2[:]
                
            b.sort(reverse=True)
                
            for p in range(0,nf):
                if c2[p]==b[0]:
                    frames[p]=pages[i]
                    faults+=1
                    break
    
    print(frames)
print(f"number of faults  {faults}")
             