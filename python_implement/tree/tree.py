from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator
from pythonds.trees.binheap import BinHeap

obj = Stack()

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, data):
        node = TreeNode(data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.leftChild is None:
                        current.leftChild = node
                        return
                    current = current.leftChild
                else:
                    if current.rightChild is None:
                        current.rightChild = node
                        return
                    current = current.rightChild

    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.leftChild is not None:
            current = current.leftChild
        return current
    
    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.rightChild is not None:
            current = current.rightChild
        return current

    def search(self, data):
        current = self.root
        while current is not None:
            if current.data == data:
                return current
            elif data < current.data:
                current = current.leftChild
            else:
                current = current.rightChild
        return current
    
class BinaryTree(object):

    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
    
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    
    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def get_root_val(self):
        return self.key
    
    def set_root_val(self, obj):
        self.key = obj

    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

class BinHeap(object):

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def percup(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                temp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = temp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.percup(self.current_size)
    
    def percdown(self, i):
        while i * 2 <= self.current_size:
            mc = self.minchild(i)
            if self.heap_list[i] > self.heap_list[mc]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = temp
            i = mc
    
    def minchild(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def buildHelp(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            self.percdown(i)
            i = i - 1

    def delmin(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.percdown(1)
        return retval



def build_parse_tree(fpexp):
    fplist = fpexp.split()
    pstack = Stack()
    etree = BinaryTree('')
    pstack.push(etree)
    current_tree = etree
    for i in fplist:
        if i == '(':
            current_tree.insert_left('')
            pstack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_val(int(i))
            parent = pstack.pop()
            current_tree.parent
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = pstack.pop()
        else:
            raise ValueError
    return etree

def evalute(parse_tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()
    if left_c and right_c:
        fn = opers[parse_tree.get_root_val()]
        return fn(evalute(left_c), evalute(right_c))
    else:
        return parse_tree.get_root_val()

def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())

def midorder(tree):
    if tree:
        midorder(tree.get_left_child())
        print(tree.get_root_val())
        midorder(tree.get_right_child())

if __name__ == '__main__':
    bh = BinHeap()
    arr = [9, 5, 6, 2, 3]
    bh.buildHelp(arr)
    i = len(arr) - 1
    while i >= 0:
        arr_min = bh.delmin()
        arr[i] = arr_min
    print(arr)
'''
    r = BinaryTree('a')
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left('b')
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.insert_right('c')
    print(r.get_right_child().get_root_val())
    #preorder(r)
    #r.preorder()
    #postorder(r)
    midorder(r)
'''