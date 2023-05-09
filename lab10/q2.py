m = int(input("Enter the number of activities: "))
timings = []
print()
print("Format of timings is (24-hr): HH:MM-HH:MM")
for i in range(m):
    timings.append(tuple(input(f"Activity timings {i+1}: ").split('-')))

# convert timings to minutes
in_minutes = []
for i in range(m):
    start, end = timings[i]
    start = int(start[:2])*60 + int(start[3:])
    end = int(end[:2])*60 + int(end[3:])
    in_minutes.append((start, end, i+1))

end_sorted = sorted(in_minutes, key=lambda x: x[1])
activity = []

# maximise number of activities
activity.append(end_sorted[0])
while i < m:
    if end_sorted[i][0] >= activity[-1][1]:
        activity.append(end_sorted[i])
    i += 1

# print(activity)
print("\nTo maximise the number of non-overlapping activities,")
print("Activities to be performed:", *list(map(lambda x: x[2], activity)))