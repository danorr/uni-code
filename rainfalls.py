rainfalls = [ [0, 9, 3, 7], [11, 9, 0, 0], [-1, 10, 12, 20],
[0, -1, 0, 0], [-1, 3, 4, 1], [2, 8, 10, 0], [-1, 0, 0, 0] ]
print("Rainfall data")
print("Day Readings Total Average")
for (day, days_rain) in enumerate(rainfalls):
    daily_total = 0
    num_readings = 0
    for rain in days_rain:
        if rain >= 0:
            daily_total += rain
            num_readings += 1
        average = daily_total / num_readings
        print("{0:2}{1:5}{2:8}{3:9.2f}".format(day, num_readings, daily_total, average))