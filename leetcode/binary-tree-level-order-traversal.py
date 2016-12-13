import collections
import pdb

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findNodeofOneLevel(self,qp):
        size = len(qp)
        i = 0
        for node in list(qp):
            if i>= size: break
            if node.left != None:
                qp.append(node.left)
            if node.right != None:
                qp.append(node.right)
            i = i+1
            qp.popleft()
        print qp
        return qp
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # q = Q.Queue()
        q = collections.deque()
        q.append(root)
        
        result = []
        if root != None:
            result = [[root.val]]
            # while not q.empty():
            while len(q) !=0:
                q = self.findNodeofOneLevel(q)
                if len(q) != 0:
                    result.append([v.val for v in q])
        return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().levelOrder(root)
    print result
