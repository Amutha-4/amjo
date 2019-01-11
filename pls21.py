Month = input("Input the Month (e.g. January, February etc.): ")
Day = int(input("Input the day: "))

if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'

if (Month == 'March') and (Day > 19):
	season = 'spring'
elif (Month == 'June') and (Day > 20):
	season = 'summer'
elif (Month == 'September') and (Day > 21):
	season = 'autumn'
elif (Month == 'December') and (Day > 20):
	season = 'winter'

print("Season is",season)
