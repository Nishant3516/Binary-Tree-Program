class BinaryTreeRootNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, val):
        if val == self.data:
            return

        if val < self.data:
            if self.left:
                self.left.add_node(val)
            else:
                self.left = BinaryTreeRootNode(val)
        else:
            if self.right:
                self.right.add_node(val)
            else:
                self.right = BinaryTreeRootNode(val)

    def search(self, val):
        if val == self.data:
            return True

        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False
        else:
            if self.right:
                self.right.search(val)
            else:
                return False

    def inorderTraversal(self):
        elements = []
        # For left side
        if self.left:
            elements += self.left.inorderTraversal()

        # For root node
        elements.append(self.data)

        # For right side
        if self.right:
            elements += self.right.inorderTraversal()
        return elements

    def preorderTraversal(self):
        elements = []
        # For root node
        elements.append(self.data)

        # For left side
        if self.left:
            elements += self.left.preorderTraversal()

        # For right side
        if self.right:
            elements += self.right.preorderTraversal()
        return elements

    def postorderTraversal(self):
        elements = []
        # For left side
        if self.left:
            elements += self.left.postorderTraversal()

        # For right side
        if self.right:
            elements += self.right.postorderTraversal()

        # For root node
        elements.append(self.data)
        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_min()
        else:
            return self.data

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def deleteNode(self, val):
        if val < self.data:
            if self.left:
                self.left.deleteNode(val)
        elif val > self.data:
            if self.right:
                self.right.deleteNode(val)
        else:
            if not self.right and not self.right:
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            
            # Using the minimum value from thr right children
            min_val = self.right.find_min()
            self.data = minVal
            self.right = self.right.deleteNode(min_val)
            
            # Using the maximum value from thr left children
            max_val = self.left.find_max()
            self.data = minVal
            self.left = self.left.deleteNode(max_val)

        return self


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinaryTreeRootNode(elements[0])

    for i in range(1, len(elements)):
        root.add_node(elements[i])

    return root


if __name__ == '__main__':
    # countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    # country_tree = build_tree(countries)

    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # print("In order traversal gives this sorted list:",numbers_tree.inorderTraversal())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
