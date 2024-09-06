#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if not tree:
        return True
  def is_bst_util(node, min_key, max_key):
    if node == -1:
        return True
        
    key, left, right = tree[node]
        
    if key < min_key or key > max_key:
        return False
    # Ensure all left subtree nodes are strictly less, and all right subtree nodes are greater or equal
    return (is_bst_util(left, min_key, key - 1) and is_bst_util(right, key, max_key))
    
  return is_bst_util(0, float('-inf'), float('inf'))


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
