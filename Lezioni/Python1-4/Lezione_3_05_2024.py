#Correzione esercizi

def construct_rectangle(area: float) -> list[float]:
    combos = []
    half_area = int(area ** 0.5)
    for width in range(1, area + 1):
        for height in range(1, area +1):
            if width * height == area and width >= height:
                return [width, height]


from collections import Counter
def find_lhs(notes: list[int]) -> int:
    num_freg = dict(Counter(notes))

    max_length = 0
    for num in num_freg:
        if num + 1 in num_freg:
            somma = num_freg[num]\
            + num_freg[num +1]
        if somma >= max_length:
            max_length = somma
        
    return max_length


def third_max(gems: list[int]) -> int:
    gems = sorted(list(set(gems)))
    if len(gems) >= 3:
        return gems[2]
    else:
        return gems[0]
    
def is_subsequence(s: str, t: str) -> bool:
    s_pointer: int = 0
    t_pointer: int = 0
    
    while s_pointer < len(s)\
    and t_pointer < len(t):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        t_pointer += 1

    return s_pointer == len(s)

#Albero binario

def search(array: list[int], x: int) -> int:
    for i in range(len(array)):
        if array[i] == x:
            return i
    return None

def binary_search(array: list[int], x: int) -> int:
    low = 0
    high = len(array)
    while low < high:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        else:
            if x > array[mid]:
                low == mid + 1
            else:
                high == mid - 1
    return None

def visit_tree(tree: dict[int, list[int]], node: int):
    print(node)
    left_child, right_child\
    = tree.get(node, [None, None])
    if left_child: #is not None
        visit_tree(tree, left_child)
    if right_child:
        visit_tree(tree, right_child)
    
tree = {4: [3,5], 3:[2, None], 5:[4.5,6], 2:[None, None], 4.5:[None, None], 6:[None, None]}
visit_tree(tree, 4)

def visit_tree_interative_L(tree: dict[int, list[int]], root: int):
    stack: list[int] = [root] # Last-In-First-Out (LIFO)
    while stack: #while len(stack) > 0
        curr_node = stack.pop()
        print(curr_node)
        left_child, right_child = tree.get(curr_node, [None, None])
        if right_child:
            stack.append(right_child)
        if left_child:
            stack.append(left_child)

tree = {4: [3,5], 3:[2, None], 5:[4.5,6], 2:[None, None], 4.5:[None, None], 6:[None, None]}
visit_tree_interative_L(tree, 4)

def visit_tree_interative_F(tree: dict[int, list[int]], root: int):
    stack: list[int] = [root] # First-In-First-Out (FIFO)
    while stack: #while len(stack) > 0
        curr_node = stack.pop(0)
        print(curr_node)
        left_child, right_child = tree.get(curr_node, [None, None])
        if right_child:
            stack.append(right_child)
        if left_child:
            stack.append(left_child)

tree = {4: [3,5], 3:[2, None], 5:[4.5,6], 2:[None, None], 4.5:[None, None], 6:[None, None]}
visit_tree_interative_F(tree, 4)


def avg_level(tree: dict[int, list[int]], root: int):
    avg_for_level: dict[int, float] = {}
    stack: list[int] = [(root, 0)]
    nood_for_level: dict[int, float] = {}
    while stack: 
        curr_node, curr_level = stack.pop(0)

        nood_for_level[curr_level] = nood_for_level.get(curr_level, 0) + 1

        left_child, right_child = tree.get(curr_node, [None, None])

        if right_child:
            stack.append((right_child, curr_level +1))
            avg_for_level[curr_level] = avg_for_level.get(curr_level, 0) + left_child
        if left_child:
            stack.append((left_child, curr_level +1))
            avg_for_level[curr_level] = avg_for_level.get(curr_level, 0) + right_child

    for level in avg_for_level:
        avg_for_level[level] /= nood_for_level[level]
    
    return avg_for_level

tree = {4: [3,5], 3:[2, None], 5:[4.5,6], 2:[None, None], 4.5:[None, None], 6:[None, None]}
avg_level(tree, 4)