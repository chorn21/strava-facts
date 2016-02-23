
class Stat(object):

	def __init__(self, stat, name, label, unit):
		self.stat = stat
		self.name = name
		self.label = label
		self.unit = unit

# TODO: refactor all these averaging functions into one function

def get_avg_time(activities, time_type):
	times = []
	avg_time = 0
	for activity in activities:
		if time_type == 'moving':
			times.append(activity.moving_time.seconds/60)
		elif time_type == 'elapsed':
			times.append(activity.elapsed_time.seconds/60)
	if len(times) > 0:
		avg_time = sum(times)/len(times)
	unit = 'minute' if avg_time == 1 else 'minutes'
	if time_type == 'moving':
		return Stat(avg_time, 'avg_moving_time', 'Average moving time', unit)
	elif time_type == 'elapsed':
		return Stat(avg_time, 'avg_elapsed_time', 'Average elapsed time', unit)

def get_avg_achievements(activities):
	counts = []
	avg_count = 0
	for activity in activities:
		counts.append(activity.achievement_count)
	if len(counts) > 0:
		avg_count = sum(counts)/len(counts)
	unit = 'achievement' if avg_count == 1 else 'achievements'
	return Stat(avg_count, 'avg_achievement_count', 'Average achievement count', unit)

def get_avg_temp(activities):
	temps = []
	avg_temp = 0
	for activity in activities:
		if activity.average_temp:
			temps.append(activity.average_temp)
	if len(temps) > 0:
		print len(temps)
		print sum(temps)
		avg_temp = sum(temps)/len(temps)
	unit = 'degree Celsius' if avg_temp == 1 else 'degrees Celsius'
	return Stat(avg_temp, 'avg_temp', 'Average activity temperature', unit)