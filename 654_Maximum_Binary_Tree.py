# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==1:
        	return TreeNode(nums[0])
        if len(nums)==0:
        	return None
        max_idx = 0
        max = num[0]
        for idx,num in enumerate(nums):
            if num > max:
            	max = num
            	max_idx = idx
     	root = TreeNode(max)
     	root.left = self.constructMaximumBinaryTree(nums[:max_idx])
     	root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
     	return root

def main():
	sol = Solution()
	nums = [3,2,1,6,0,5]
	root = sol.constructMaximumBinaryTree(nums)

if __name__ == "__main__":
    main()
