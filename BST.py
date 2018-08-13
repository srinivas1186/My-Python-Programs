
class Node:
    """
    Class for creating nodes in Tree
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree(object):
    """
     This is a Class for Binary Search Tree
     This takes initially a single value which is the root node
    """

    def __init__(self, root, *remaining):
        """
        Intialisation Function for the tree which can take one or more values
        :param root: Root Element in the Tree
        :param remaining: Remaining Elements to be inserted.
        """
        self.root = Node(root)
        self.height = 0
        for i in list(remaining):
            self.ninsert(i)

    def insert(self, first, *remaining):
        """
        Function to insert one or more elements into the tree in the given order
        :param first: First Element to insert
        :param remaining: Remaining Elements to Insert
        :return: It returns NoneType
        """
        self.ninsert(first)
        for i in list(remaining):
            self.ninsert(i)

    def ninsert(self, value):
        """
        Function which actually implements Insertion Of Tree
        :param value:
        :return:
        """
        height = 0
        root = self.root
        before = root
        while root:
            before = root
            if root.key <= value:
                root = root.right
            else:
                root = root.left
            height += 1
        if before.key <= value:
            before.right = Node(value)
        else:
            before.left = Node(value)
        if self.height < height:
            self.height = height

    def __repr__(self):
        print("Printing In-order of the tree is :")
        Tree.in_order(self.root)
        print("\nPrinting Pre-order of the tree is :")
        Tree.pre_order(self.root)
        print("\nPrinting Post-order of the tree is :")
        Tree.post_order(self.root)
        print("\nPrinting Level-order of the tree is :")
        Tree.level_order(self.root)
        print()
        return ''

    def level_order_by_line(self):
        Tree.lbllo(self.root)

    def tree_structure(self):
        Tree.structure(self.root,self.height)

    @staticmethod
    def structure(root, tree_height):
        que = []
        level = 0
        space = '    '
        que.append(root)
        while any(map(lambda x: x != space, que)):
            level_length = len(que)
            for i in range(level_length):
                if que[i] is space:
                    que.append(space)
                    que.append(space)
                    continue
                if que[i].left:
                    que.append(que[i].left)
                else:
                    que.append(space)
                if que[i].right:
                    que.append(que[i].right)
                else:
                    que.append(space)
            ex = 2**level
            while ex:
                if que[0] is space:
                    print(space * (2 ** tree_height - 1) + str(que.pop(0)).center(4, ' ') + space * (2 ** tree_height ), end='')
                else:
                    print(space * (2 ** tree_height - 1) + str(que.pop(0).key).center(4, ' ') + space * (
                                2 ** tree_height ), end='')
                ex -= 1
            print()
            level += 1
            tree_height -= 1


    @staticmethod
    def lbllo(root):
        """
        lbllo -> line by line level order
        Function to print line by line level order of a tree
        :param root:
        :return:
        """
        level = 0
        que = []
        que.append(root)
        while que:
            print("At level %4d -->" % level, end=" ")
            level_length = len(que)
            for i in range(level_length):
                if que[0].left:
                    que.append(que[0].left)
                if que[0].right:
                    que.append(que[0].right)
                print(que.pop(0).key, end=" ")
            print()
            level += 1


    @staticmethod
    def in_order(root):
        if root:
            Tree.in_order(root.left)
            print(root.key, end=' ')
            Tree.in_order(root.right)

    @staticmethod
    def pre_order(root):
        if root:
            print(root.key, end=' ')
            Tree.pre_order(root.left)
            Tree.pre_order(root.right)

    @staticmethod
    def post_order(root):
        if root:
            Tree.post_order(root.left)
            Tree.post_order(root.right)
            print(root.key, end=' ')

    @staticmethod
    def level_order(root):
        que = []
        que.append(root)
        while que:
            if que[0].left:
                que.append(que[0].left)
            if que[0].right:
                que.append(que[0].right)
            print(que.pop(0).key, end=' ')


t = Tree(20, 10)
t.insert(5, 21, 1, 6, 60)
t.insert(30)
t.insert(12, 11, 13)
print(t)
t.level_order_by_line()
print(t.height)
t.tree_structure()
