m = int(input("Enter the number of activities: "))
timings = []
print()
print("Format of timings is (24-hr): HH:MM-HH:MM")
for i in range(m):
    timings.append(tuple(input(f"\tActivity{i+1}: ").split('-')))
weights = list(map(int, input("Enter the weights of each activity: ").split()))

# convert timings to minutes
in_minutes = []
for i in range(m):
    start, end = timings[i]
    start = int(start[:2])*60 + int(start[3:])
    end = int(end[:2])*60 + int(end[3:])
    in_minutes.append((start, end, weights[i], i+1))

end_sorted = sorted(in_minutes, key=lambda x: x[1])
activity = []

# Previuos greedy implementation does not work here
# Here, we need to apply greedy as well as DP to take weights also in to account

dp = [None]*m
dp[0] = end_sorted[0][2]

for i in range(1,m):
    cur_prof = end_sorted[i][2]
    for j in range(i):
        if end_sorted[j][1] <= end_sorted[i][0]:
            cur_prof += dp[j]
            break
    if cur_prof > dp[i-1]:
        dp[i] = cur_prof
        activity.append(end_sorted[i])
    else:
        dp[i] = dp[i-1]

# print(activity)
print("\nTo maximise the weight of non-overlapping activities,")
print("Activities to be performed:", *[x[3] for x in activity])
print("Maximum weight:", sum([x[2] for x in activity]))