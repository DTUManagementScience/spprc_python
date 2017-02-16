class Label:
	def __init__(self, cost: float, reduced_cost: float, resources: [float], dominated = False):
		self.cost = cost
		self.reduced_cost = reduced_cost
		self.resources = resources
		self.dominated = dominated

def __spprc_label_is_label_dominating(self, other: Label):
	if self.reduced_cost > other.reduced_cost:
		return False
	for i in range(len(self.resources)):
		if self.resources[i] > other.resources[i]:
			return False
	return True

def __spprc_label_check_dominance(label1: Label, label2: Label) -> bool:
	if not label1.dominated and not label2.dominated:
		if label1.is_dominating(label2):
			label2.dominated = True
		elif label2.is_dominating(label1):
			label1.dominated = True

Label.is_dominating = __spprc_label_is_label_dominating
Label.check_dominance = __spprc_label_check_dominance

