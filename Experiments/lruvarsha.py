# Initialize variables
np = nf = k = i = j = p = q = r = faults = c1 = 0
pages = [0] * 10
frames = [-1] * 10
c2 = [0] * 10
b = [0] * 10

# Input number of pages and frames
np = int(input("Enter the number of pages: "))
nf = int(input("Enter the number of frames: "))

# Input reference string
print("Enter the reference string:")
for i in range(np):
    pages[i] = int(input())

# Initialize frames with -1 (empty)
for i in range(nf):
    frames[i] = -1

# Insert first page into frames
frames[k] = pages[k]
k += 1
faults += 1

# Iterate through the reference string
for i in range(1, np):
    c1 = 0

    # Check if the page already exists in memory
    for r in range(nf):
        if frames[r] != pages[i]:
            c1 += 1
        else:
            break

    # Page doesn't exist in memory
    if c1 == nf:
        # Check if memory is empty
        if k < nf:
            frames[k] = pages[i]
            k += 1
            faults += 1
        else:
            # Apply LRU
            for r in range(nf):
                c2[r] = 0
                for j in range(i - 1, -1, -1):
                    if frames[r] != pages[j]:
                        c2[r] += 1
                    else:
                        break

            # Copy c2 to b
            b = c2[:]

            # Sort b in descending order
            b.sort(reverse=True)

            # Find the frame to replace
            for r in range(nf):
                if c2[r] == b[0]:
                    # Replace
                    frames[r] = pages[i]
                    faults += 1
                    break

    # Print frames after inserting the page
    print(f"Frames after inserting page {pages[i]}:", frames[:nf])

# Output page fault count
print("Page fault count:", faults)
