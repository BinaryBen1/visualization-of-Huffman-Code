import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def generate_frequency_table(text):
    if not text:
        raise Exception("The Input-String is empty.")
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

def generate_huffman_tree():
    Knoten = [Node(char, freq) for char, freq in frequency_table.items()]
    
    while len(Knoten) > 1:
        Knoten = sorted(Knoten, key=lambda x: x.freq, reverse=True)
        left = Knoten.pop()
        right = Knoten.pop() if len(Knoten) > 0 else None
        merged = Node(left.char + (right.char if right else ''), left.freq + (right.freq if right else 0))
        merged.left = left
        merged.right = right
        Knoten.append(merged)

    return Knoten[0] if Knoten else None

def plot_tree_3d(node, x=0, y=0, z=0, ax=None, depth=1, branch_length=1, node_counts=None):
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

    if node.char is not None:
        text_node = node.char + ':' + str(node.freq)
        ax.text(x, y, z + 0.03, text_node)

    if node_counts is None:
        node_counts = {}

    if depth not in node_counts:
        node_counts[depth - 1] = 0

    if node is not None:
        ax.scatter(x, y, z, color='black')

        if node.left is not None:
            node_counts[depth + 1] = node_counts.get(depth + 1, 0)
            left_x = x - 1 / (2 ** depth)  
            left_y = y - 1 / (2 ** depth)  
            left_z = z - 1 / (2 ** depth)  
            ax.plot([x, left_x], [y, left_y], [z, left_z], color='blue')
            ax.text((x + left_x) / 2, (y + left_y) / 2, (z + left_z) / 2 + 0.03, '0', color='blue')
            plot_tree_3d(node.left, left_x, left_y, left_z, ax, depth + 1, branch_length, node_counts)

        if node.right is not None:
            node_counts[depth + 1] = node_counts.get(depth + 1, 0)
            right_x = x + 1 / (2 ** depth)
            right_y = y - 1 / (2 ** depth)  
            right_z = z - 1 / (2 ** depth)  
            ax.plot([x, right_x], [y, right_y], [z, right_z], color='red')
            ax.text((x + right_x) / 2, (y + right_y) / 2, (z + right_z) / 2 + 0.03, '1', color='red')
            plot_tree_3d(node.right, right_x, right_y, right_z, ax, depth + 1, branch_length, node_counts)

    return ax

def encoding_huffman_text(root, text):
    encoding = []

    def find_child(node, char):
        nonlocal encoding

        if node is None:
            return

        if node.char == char:
            return  # Reached the character, stop

        if char in (node.left.char if node.left else ''):
            encoding.append(0)
            find_child(node.left, char)
        elif char in (node.right.char if node.right else ''):
            encoding.append(1)
            find_child(node.right, char)

    for char in text:
        find_child(root, char)
    return encoding


# Huffman Code algorithm
# Example text
text = input("Enter a text to code in Huffman: ")

frequency_table = generate_frequency_table(text)
root = generate_huffman_tree()
encoding = encoding_huffman_text(root, text)

fig = plt.figure(figsize=(10, 5))
plt.title('3D Binary Tree Visualization')

ax1 = fig.add_subplot(121, projection='3d')
ax1 = plot_tree_3d(root, ax=ax1)
ax1.axis('off')

ax2 = fig.add_subplot(122)
ax2.axis('off')
ax2.table(cellText=[[char, freq] for char, freq in frequency_table.items()],
          colLabels=['Buchstabe', 'Häufigkeit'],
          loc='center')
print(encoding)
ax3 = fig.add_subplot(122)
ax3.axis('off')

plt.text(0.4, 0.3, text +' = '+ ''.join(str(x) for x in encoding) , ha='center', va='center', fontsize=15)

plt.axis('off')
plt.show()
