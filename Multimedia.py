import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def generate_frequency_table(text):
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
        left = Knoten.pop()
        right = Knoten.pop()
        merged = Node(left.char + right.char, left.freq + right.freq)
        merged.left = left
        merged.right = right
        if len(Knoten) == 0:
            return merged
        for index, x in enumerate(Knoten):
            if x.freq <= merged.freq:
                Knoten.insert(index, merged)
                break

def plot_tree_3d(node, x=0, y=0, z=0, ax=None, depth=1, branch_length=1, node_counts=None):
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

    if node.char is not None:
        text_node = node.char + ':' + str(node.freq)
        ax.text(x, y, z + 0.1, text_node)

    if node_counts is None:
        node_counts = {}

    if depth not in node_counts:
        node_counts[depth - 1] = 0

    if node is not None:
        ax.scatter(x, y, z, color='black')

        if node.left is not None:
            node_counts[depth + 1] = node_counts.get(depth + 1, 0)
            left_x = x - 1 / (2 ** depth)  # Adjusting x-coordinate based on depth
            left_y = y - 1 / (2 ** depth)  # Adjusting y-coordinate based on depth
            left_z = z - 1 / (2 ** depth)  # Adjusting z-coordinate based on depth
            ax.plot([x, left_x], [y, left_y], [z, left_z], color='blue')
            ax.text((x + left_x) / 2, (y + left_y) / 2, (z + left_z) / 2 + 0.1, '0', color='blue')
            plot_tree_3d(node.left, left_x, left_y, left_z, ax, depth + 1, branch_length, node_counts)

        if node.right is not None:
            node_counts[depth + 1] = node_counts.get(depth + 1, 0)
            right_x = x + 1 / (2 ** depth)  # Adjusting x-coordinate based on depth
            right_y = y - 1 / (2 ** depth)  # Adjusting y-coordinate based on depth
            right_z = z - 1 / (2 ** depth)  # Adjusting z-coordinate based on depth
            ax.plot([x, right_x], [y, right_y], [z, right_z], color='red')
            ax.text((x + right_x) / 2, (y + right_y) / 2, (z + right_z) / 2 + 0.1, '1', color='red')
            plot_tree_3d(node.right, right_x, right_y, right_z, ax, depth + 1, branch_length, node_counts)

    return ax

# Huffman Code algorithm
text = "MISSISSIPPI"
frequency_table = generate_frequency_table(text)
root = generate_huffman_tree()

fig = plt.figure(figsize=(10, 5))
plt.title('3D Binary Tree Visualization')

# Add subplot for the 3D tree visualization
ax1 = fig.add_subplot(121, projection='3d')

# Plot the Huffman tree in 3D
ax1 = plot_tree_3d(root, ax=ax1)

# Add subplot for the frequency table
ax2 = fig.add_subplot(122)
ax2.axis('off')
ax2.table(cellText=[[char, freq] for char, freq in frequency_table.items()],
          colLabels=['Buchstabe', 'Häufigkeit'],
          loc='center')

plt.show()


"""
singe character words do not work
MISSISSIPPI does not work 4 different characters
"""