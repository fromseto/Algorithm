import Queue as Q
import pdb

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findNodeofOneLevel(self,qp):
        size = qp.qsize()
        i = 0
        for node in iter(qp.get,None):
            if i>= size: break
            if node.left != None:
                qp.put(node.left)
            if node.right != None:
                qp.put(node.right)
            i = i+1
        qp.pop(node)
        print qp
        return qp
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = Q.Queue()
        q.put(root)
        
        pdb.set_trace()
        result = [[root.val]]
        while not q.empty():
            q = self.findNodeofOneLevel(q)
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
