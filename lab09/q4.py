n = int(input("Enter the number of classrooms: "))
m = int(input("Enter the number of lecture timings: "))
timings = []
print()
print("Format of timings is (24-hr): HH:MM-HH:MM")
for i in range(m):
    timings.append(tuple(input(f"Lecture timings {i+1}: ").split('-')))

# convert timings to minutes
minutes, duration = [], []
for i in range(m):
    start, end = timings[i]
    start = int(start[:2])*60 + int(start[3:])
    end = int(end[:2])*60 + int(end[3:])
    minutes.append((start, end))
    duration.append(end - start)

start_sorted = sorted(minutes, key=lambda x: x[0])
cls_num = 0
cls_rooms = []

while len(start_sorted) != 0:
    cls_rooms.append([])
    start_ind = 0
    while True:
        now_cls = start_sorted.pop(start_ind)
        cls_rooms[cls_num].append(now_cls)
        try:
            next_cls = min(start_sorted, key=lambda x: x[0]-now_cls[1] if x[0]-now_cls[1] >= 0 else 2000)
        except ValueError:
            break
        if next_cls[0]-now_cls[1] > 0:
            start_ind = start_sorted.index(next_cls)
        else:
            break
    cls_num += 1

# print(cls_rooms)
if cls_num < n:
    print("Minimum number of classrooms required:", cls_num)
else:
    print("Minimum number of classrooms required:", n)
    print("Extra classrooms required:", cls_num-n)