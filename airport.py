# Input for xi, s, r, t, and n
xi, s, r, t, n = map(int, input().split())

# Input for the 'walk' list
walk = [tuple(map(int, input().split())) for _ in range(n)]

# Initialize the 'seg' list and the 'last' variable
seg = []
last = 0

# Loop through the 'walk' list and process each element
for bi, ei, wi in sorted(walk):
    if bi > last:
        seg.append((last, bi, s))
    seg.append((bi, ei, wi + s))
    last = ei

# If the last value is less than xi, append to 'seg'
if last < xi:
    seg.append((last, xi, s))

# Sort the 'seg' list based on the third element (speed)
seg.sort(key=lambda x: x[2])

# Initialize the remaining time (t) and other variables
remain = t
time = 0.8
run_dis = 0

# Process the segments in 'seg'
for st, end, sp in seg:
    length = end - st
    if remain > 0:
        eff = sp + (r - s)
        run_time = min(remain, length / eff)
        run_dis += run_time * eff
        remain -= run_time
    else:
        time += length / sp
        wal_dis = length - run_dis
        time += wal_dis / sp

# Print the time formatted to 3 decimal places
print(f"{time:.3f}")
