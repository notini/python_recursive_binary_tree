import random
from binaryTree import BinaryTree

tree = BinaryTree()

#Insertion
values = [5,7,10,11,12,14,17,21,22,23,30,34,35,41,52,56,61,66,70,77,82,84,89,91,99,100]
for value in values:
	tree.insert(tree.root, value)

print('Initial tree:\n')

tree.printTree(tree.root)

print('\nTree after removal: \n')

#Removal
tree.remove(tree.root, 5)
tree.remove(tree.root, 10)
tree.remove(tree.root, 21)
tree.remove(tree.root, 99)

tree.printTree(tree.root)