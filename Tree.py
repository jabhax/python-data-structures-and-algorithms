''' Trees '''
import time


# Binary Tree Node Implementation
class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.value = v

# Binary Search Tree Implementation
# Includes:
# - Breadth-First-Search (BFS-Iterative)
# - Breadth-First-Search (BFS-Recursive)
# - Depth-First-Search (DFS)
class BST:
    # Constructor
    def __init__(self):
        self.root = None

    # Insert Implementation
    def insert(self, v):
        new_node = Node(v)
        if not self.root:
            self.root = new_node
        else:
            curr = self.root
            while True:
                if v == curr.value:
                    return self
                elif v < curr.value:
                    if not curr.left:
                        curr.left = new_node
                        return self
                    curr = curr.left
                else:
                    if not curr.right:
                        curr.right = new_node
                        return self
                    curr = curr.right

    # Lookup Implementation
    def lookup(self, v):
        if not self.root:
            return False
        curr = self.root
        while curr:
            if v == curr.value :
                print('found')
                return True
            elif v < curr.value:
                print('left')
                curr = curr.left
            else:
                print('right')
                curr = curr.right
        else:
            return False

    def remove(self, v):
        if self.root == None:
            return False
        curr = self.root
        parent = None
        while not curr == None:
            if v == curr.value: # If we are at the remove node check its L and R children.
                if curr.right == None: # If remove node has no right child check local parent.
                    if parent == None: # If no local parent set, then point root to the curr node's left child.
                        self.root = curr.left
                    else: # Otherwise, there is a local parent and we compare its values.
                        if curr.value < parent.value: # If current is less than parent, then point parent's left child to current's left child.
                            parent.left = curr.left
                        elif curr.value > parent.value: # If current is greater than parent, then point parent's right child to current's left child.
                            parent.right = curr.left
                elif curr.right.left == None: # If remove node has right child, but the right child has no left child, check local parent.
                    if parent == None: # If no local parent set, then set root to the curr node's left child.
                        self.root = curr.left
                    else: # Otherwise, there is a local parent and we compare its values.
                        curr.right.left = curr.left
                        if curr.value < parent.value: # If current is less than parent, then point parent's left child to the current's right child.
                            parent.left = curr.right
                        elif curr.value > parent.value: # If current is greater than parent, then point parents right child to the current's right child.
                            parent.right = curr.right
                else: # If remove node has right and left child, then we find the right child's left most child.
                    lm = curr.right.left  # left-most
                    lmp = curr.right  # left-most-parent
                    while lm.left:
                        lmp = lm
                        lm = lm.left
                        # Point left-most-parent's left subtree to the left-most's right subtree
                    lmp.left = lm.right
                    lm.left = curr.left
                    lm.right = curr.right
                    if parent == None: # If local parent is not set then set root to left-most.
                        self.root = lm
                    else: # Otherwise, there is a local parent and we compare its values.
                        if curr.value < parent.value: # If current is less than parent, then point parent's left child to the left-most child.
                            parent.left = lm
                        elif curr.value > parent.value: # If current is greater than parent, then point parent's right child to the left-most child.
                            parent.right = lm
                return True
            elif v < curr.value: # Value is less than current, move left.
                parent = curr
                curr = curr.left
            else: # Value is greater than current, move right.
                parent = curr
                curr = curr.right

    ''' Breadth First Search (BFS) '''
    def bfs(self):
        curr = self.root
        result, queue = [], [curr]
        while len(queue) > 0:
            curr = queue.pop()
            result.append(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return result

    ''' Breadth First Search - Recursive (BFS) '''
    def bfs_r(self, queue=[], result=[]):
        if len(queue) <= 0:
            return queue
        curr = queue.pop()
        result.append(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        self.bfs_r(queue, result)
        return result

    ''' Depth First Search (DFS) '''
    def dfs(self, order='in'):
        # DFS: POST-ORDER sub-routine
        def _dfs_postorder(n, result):
            if n.left:
                _dfs_postorder(n.left, result)
            if n.right:
                _dfs_postorder(n.right, result)
            result.append(n.value)

        # DFS: IN-ORDER sub-routine
        def _dfs_inorder(n, result):
            if n.left:
                _dfs_inorder(n.left, result)
            result.append(n.value)
            if n.right:
                _dfs_inorder(n.right, result)

        # DFS: PRE-ORDER sub-routine
        def _dfs_preorder(n, result):
            result.append(n.value)
            if n.left:
                _dfs_preorder(n.left, result)
            if n.right:
                _dfs_preorder(n.right, result)

        # DSF Order Selection
        curr, result = self.root, []
        if order == 'post':
            _dfs_postorder(curr, result)
        if order == 'in':
            _dfs_inorder(curr, result)
        if order == 'pre':
            _dfs_preorder(curr, result)
        return result

    # Simple Traversal that prints all the values recursively.
    def traverse(self):
        def _tr(n, r):
            r.append(n.value)
            if n.left: _tr(n.left, r)
            if n.right: _tr(n.right, r)
        result = []
        _tr(self.root, result)
        print(f'Traversed: {result}')


# Helper function for calculating end-time from start-time using time.time()
def _et(start_time, tr=7):
    end_time = round(time.time()-start_time, tr)
    start_time = time.time()
    return end_time

# Main
def main():
    # Values being used to popular sample BST.
    bst_values = [9, 4, 6, 20, 170, 15, 1]
    bst = BST()
    # Test Insert Implementation
    st = time.time()
    for v in bst_values:
        bst.insert(v)
    print(f'BST Array: {bst_values}')

    # Test Tree Traversal Implementations.
    st = time.time()
    bst.traverse()
    print(f'Elapsed: ({_et(st)}s): Do Simple Traverse')
    # Test BFS Implementations.
    st = time.time()
    bfs = bst.bfs()
    print(f'Elapsed: ({_et(st)}s): BFS on BST: {bfs}')
    # Test Recursive-BFS Implementations.
    st = time.time()
    bfs_r = bst.bfs_r([bst.root])
    print(f'Elapsed: ({_et(st)}s): BFS-Recursive on BST: {bfs_r}')
    # Test DFS: Inorder Implementations.
    st = time.time()
    dfs_inorder = bst.dfs()
    print(f'Elapsed: ({_et(st)}s): DFS on BST (inorder): {dfs_inorder}')
    # Test DFS: Postorder Implementations.
    st = time.time()
    dfs_post = bst.dfs(order="post")
    print(f'Elapsed: ({_et(st)}s): DFS on BST (postorder): {dfs_post}')
    # Test DFS: Preorder Implementations.
    st = time.time()
    dfs_pre = bst.dfs(order="pre")
    print(f'Elapsed: ({_et(st)}s): DFS on BST (preorder): {dfs_pre}')


if __name__ == '__main__':
    main()
