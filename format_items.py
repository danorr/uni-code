def format_list(items):
	if len(items) == 1:
		return "{0}".format(items[0])
	else:
		return "{0:<10}|{1:>10}".format(items[0], items[1])