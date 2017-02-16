from spprc.label import Label
from enum import Enum
class WindowType(Enum):
	Hard = 1
	Soft = 2

class Node:
	def __init__(self, name: str, window_starts: [float], window_ends: [float], window_types: [WindowType]):
		if len(window_starts) != len(window_ends):
			raise ValueError("The length of the window end array does not match the length of the window start array")
		if len(window_starts) != len(window_types):
			raise ValueError("The length of the window type array does not match the length of the window start array")
		self.name = name
		self.window_starts = window_starts
		self.window_ends = window_ends
		self.window_types = window_types

	def is_feasible(self, label: Label) -> bool:
		for i in range(len(label.resources)):
			if label.resources[i] > self.window_ends[i]:
				return False
			if label.resources[i] < self.window_starts[i]:
				if self.window_types[i] == WindowType.Hard:
					return False
				label.resources[i] = self.window_starts[i]
		return True
			

class Arc:
	def __init__(self, from_node: Node, to_node: Node, extension_function):
		self.from_node = from_node
		self.to_node = to_node
		self.name = "{}->{}".format(self.from_node.name, self.to_node.name)
		self.extension = extension_function
	
	def extend(self, label: Label):
		new_label = self.extension(label)
		result = self.to_node.is_feasible(new_label)
		return new_label, result
		
