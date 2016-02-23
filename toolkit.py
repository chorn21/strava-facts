
def get_activity_types(activities, a_type):
	type_list = list()
	for a in activities:
		if a.type.lower() == a_type:
			type_list.append(a)
	return type_list