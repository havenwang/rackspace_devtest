# Assumption: input is valid breadth first heap style representation
# Runtime of this code is O(n^2), where at most n nodes

# INPUT FILE SHOULD BE NAMED 'example.txt' AND BE IN SAME DIRECTORY
# OUTPUT SENT TO FILE 'output.txt'

import sys

class TreeNode:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

   # add left and right children nodes given their values
   def addNewNode(self, child_left_value, child_right_value):
      if not child_left_value == '':
         new_node = TreeNode(child_left_value)
         self.left = new_node
      if not child_right_value == '':
         new_node = TreeNode(child_right_value)
         self.right = new_node

# given a valid breadth first heap style representation of a binary tree,
# construct the tree and return the root node
def constructTree(input_arg):
   values = input_arg.split(',')
   
   incr = 0
   root_node = TreeNode(values[incr])
   prev_layer = []
   current_layer = [root_node]

   # build tree layer by layer starting from the root
   while incr < len(values)-1:
      prev_layer = current_layer
      current_layer = []
      for node in prev_layer:
         incr += 2
         if not node:
            current_layer.append(None)
            current_layer.append(None)
         else:
            node.addNewNode(values[incr-1], values[incr])
            current_layer.append(node.left)
            current_layer.append(node.right)

   return root_node

# given two binary trees, t1 and t2, check if t1 is a subtree of t2 
def compareSubtree(t1, t2):
   to_check = [t2]

   # conduct breadth first search of t2 and compare t1 at each node
   while to_check:
      curr_node = to_check.pop(0)
      if isSubtree(curr_node, t1):
         return True

      # add any children of current node to list of nodes to check
      if not curr_node.left == None:
         to_check.append(curr_node.left)
      if not curr_node.right == None:
         to_check.append(curr_node.right)

   return False
   
# check if t1 is a valid subtree at curr_node
def isSubtree(curr_node, t1):
   t1_BFS = [t1]
   t2_BFS = [curr_node]

   while t1_BFS:
      t1_node = t1_BFS.pop(0)
      t2_node = t2_BFS.pop(0)
      # if node from t2 is empty or if value is different then t1 not subtree
      if not t2_node or t1_node.value != t2_node.value:
         return False

      # continue comparing deeper for both trees
      if not t1_node.left == None:
         t1_BFS.append(t1_node.left)
         t2_BFS.append(t2_node.left)
      if not t1_node.right == None:
         t1_BFS.append(t1_node.right)
         t2_BFS.append(t2_node.right)

   return True

# Read input, first line is t2, second line is t1
trees = []
with open('example.txt','r') as f:
    for line in f:
        trees.append(line)
t2 = constructTree(trees[0])
t1 = constructTree(trees[1])

sys.stdout = open('output.txt', 'w')
print compareSubtree(t1,t2)
