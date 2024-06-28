def find_first_free_slot(timetable):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    free_periods = [[True]*10 for _ in range(6)]
    for day in range(6):
        free_periods[day][5] = False 

    for day, schedule in enumerate(timetable):
        slots = schedule.strip().split("][")
        for slot in slots:
            slot = slot.strip('[]')
            if '-' in slot:
                start, end = map(int, slot.split('-'))
                for i in range(start, end+1):
                    free_periods[day][i-1] = False
            else:
                free_periods[day][int(slot)-1] = False

    for day in range(6):
        for period in range(10):
            if free_periods[day][period]:
                return f"{days[day]} {period+1}"
    
    return "No Free Slots"

n = 6 
timetable = []
for i in range(n):
    timetable.append(input().strip())

res = str(find_first_free_slot(timetable))
print(res)
