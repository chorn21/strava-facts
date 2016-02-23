from analysis import stats

class ActivityList(StravaObject):

	def __init__(self, client):
		self.data_obj = client.get_activities()
		self.activities = []
		for activity in self.data_obj:
			self.activities.append(Activity(data_obj=activity))


class ActivitySet(object):

	def __init__(self, a_type, activities):
		self.activity_type = a_type
		self.activities = activities
		self.stats = [stats.get_avg_time(activities, 'moving')
						, stats.get_avg_time(activities, 'elapsed')
						, stats.get_avg_achievements(activities)
						, stats.get_avg_temp(activities)
					]
