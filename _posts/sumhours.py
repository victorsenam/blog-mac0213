import sys
import re

mins = 0
for line in sys.stdin:
	for time in re.findall(r'\*\*\d*h\d*\*\*', line):
		split_time = time.split("h")
		mins += int(split_time[0][2:])*60
		mins += int(split_time[1][:-2])

print(mins)
