
class Node:
	
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		
class BinaryTree:

	def __init__(self):
		self.root = None
	
	#Inserts value to tree.
	def insert(self, currNode, value):
		#no root yet
		if self.root == None:
			self.root = Node(value)
		else:
			if value < currNode.value:
				if currNode.left == None:
					currNode.left = Node(value)
				else:
					self.insert(currNode.left, value)
			else:
				if currNode.right == None:
					currNode.right = Node(value)
				else:
					self.insert(currNode.right, value)
					
	#Checks if value is in tree.
	def find(self, currNode, value):
		if currNode.value == value:
			return currNode
		if value < currNode.value and currNode.left is not None:
			return self.find(currNode.left, value)
		elif value > currNode.value and currNode.right is not None:
			return self.find(currNode.right, value)
		
	#Removes value from tree.
	def remove(self, currNode, value):
		if self.root == None:
			print('Cant remove from empty tree!')
		else:
			if self.root.value == value:
				auxRoot = Node(0)
				auxRoot.left = self.root
				result = self._remove(self.root, value, auxRoot)
				self.root = auxRoot.left
				return result	
			else:
				return self._remove(currNode, value, None)
				
	def _remove(self, currNode, value, parent):
		if value < currNode.value:
			if currNode.left is not None:
				return self._remove(currNode.left, value, currNode)
		elif value > currNode.value:
			if currNode.right is not None:
				return self._remove(currNode.right, value, currNode)
		else:
			if currNode.left is not None and currNode.right is not None:
				currNode.value = self.minValue(currNode.right)
				return self._remove(currNode.right, currNode.value, currNode)
			elif parent.left == currNode:
				if currNode.left is not None:
					parent.left = currNode.left
				else:
					parent.left = currNode.right
			elif parent.right == currNode:
				if currNode.right is not None:
					parent.right = currNode.right
				else:
					parent.right = currNode.left
				
	#Returns min value found in tree.
	def minValue(self, node):
		if node.left is None:
			return node.value
		else:
			return self.minValue(node.left)	
		
	#Prints tree in crescent order.
	def printTree(self, node):
		if self.root == None:
			print('Empty Tree!')
		else:
			if node is not None:
				self.printTree(node.left)
				print(node.value)
				self.printTree(node.right)