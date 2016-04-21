# -*- coding:utf-8 -*-
 
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class LongestPath:
    def findPath(self, root):
        # write code here
        maxLen = [0]
        def getPath(root):
            if root == None:
                return 0
            left = 0
            right = 0
            if root.left != None:
                left = getPath(root.left)
                if root.left.val != root.val:
                    left = 0
            if root.right != None:
                right = getPath(root.right)
            	if root.right.val != root.val:
                    right = 0
            maxLen[0] = max(maxLen[0], left + right + 1)
            return max(left, right) + 1
        
        if root == None:
            return 0
        getPath(root)
        return maxLen[0]
