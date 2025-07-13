def min_time_to_gate(X, S, R, t, N, walkways):
    segments = []

    # Step 1: Add walkway segments
    for B, E, W in walkways:
        segments.append((B, E, W))

    # Step 2: Add non-walkway segments
    covered = [False] * X
    for B, E, W in walkways:
        for i in range(B, E):
            covered[i] = True

    i = 0
    while i < X:
        if not covered[i]:
            start = i
            while i < X and not covered[i]:
                i += 1
            segments.append((start, i, 0))  # Wi = 0
        else:
            i += 1

    # Step 3: Convert segments to (length, Wi)
    seg_list = []
    for B, E, W in segments:
        seg_list.append((E - B, W))

    # Step 4: Sort segments by walkway speed (Wi), ascending
    seg_list.sort(key=lambda x: x[1])

    # Step 5: Distribute running time greedily
    remaining_run_time = t
    total_time = 0.0

    for length, W in seg_list:
        run_speed = R + W
        walk_speed = S + W

        run_time_for_seg = length / run_speed

        if remaining_run_time >= run_time_for_seg:
            # Can run full segment
            total_time += run_time_for_seg
            remaining_run_time -= run_time_for_seg
        else:
            # Run part of the segment
            run_distance = remaining_run_time * run_speed
            walk_distance = length - run_distance

            total_time += remaining_run_time + (walk_distance / walk_speed)
            remaining_run_time = 0.0

    return round(total_time, 3)

X, S, R, t, N = map(int, input().split())
walkways = []
for _ in range(N):
    B, E, W = map(int, input().split())
    walkways.append((B, E, W))

# Compute and print result
result = min_time_to_gate(X, S, R, t, N, walkways)
print(f"{result:.3f}")
