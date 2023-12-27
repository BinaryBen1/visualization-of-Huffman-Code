import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    

    # Funktion zur Erstellung der Buchstaben-Häufigkeits-Tabelle
def generate_frequency_table(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return dict(sorted(frequency.items(), key=lambda x:x[1],reverse=True))


def generate_huffman_tree():
    print('Bauen Baumstruktur vom frequency table: ',frequency_table)
    Knoten = [Node(char, freq) for char, freq in frequency_table.items()]
    
    while len(Knoten)>1:
        left=Knoten.pop()
        right=Knoten.pop()
        merged = Node(left.char+right.char, left.freq + right.freq)
        merged.left = left
        merged.right = right
        if len(Knoten)==0:
            Knoten.append(merged)
            break
        for index, x in enumerate(Knoten):
            if x.freq<=merged.freq:
                Knoten.insert(index, merged)
                break
    print("generated huffman tree")
    return Knoten[0]

def plot_huffman_tree(node, x=0, y=0, ax=None, depth=0, node_counts=None):
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

    if node.char is not None:
        text_node = node.char + ':' + str(node.freq)
        ax.text(x, y, depth, text_node)

    if node_counts is None:
        node_counts = {}

    if depth not in node_counts:
        node_counts[depth] = 0

    if node.left:
        node_counts[depth + 1] = node_counts.get(depth + 1, 0)
        x_left = x - (2 ** (depth + 1 - 1))
        ax.plot([x, x_left], [y, y + 1], [depth, depth + 1], marker='o')
        ax.text((x + x_left) / 2, (y + (y + 1)) / 2, (depth + (depth + 1)) / 2, '0')
        plot_huffman_tree(node.left, x_left, y + 1, ax, depth + 1, node_counts)

    if node.right:
        node_counts[depth + 1] = node_counts.get(depth + 1, 0)
        x_right = x + (2 ** (depth + 1 - 1))
        ax.plot([x, x_right], [y, y + 1], [depth, depth + 1], marker='o')
        ax.text((x + x_right) / 2, (y + (y + 1)) / 2, (depth + (depth + 1)) / 2, '1')
        plot_huffman_tree(node.right, x_right, y + 1, ax, depth + 1, node_counts)

    return ax


#problem nodes colliden

# Beispieltext als Eingabe
text = "MISSISSIXXI"                        #für 4 unterschiedliche Buchstaben gehts nicht, liegt wahrscheinlich am plot

fig = plt.figure(figsize=(10, 5))

# Buchstaben-Häufigkeits-Tabelle erstellen und anzeigen
frequency_table = generate_frequency_table(text)
ax2 = fig.add_subplot(122)
ax2.axis('off')
ax2.table(cellText=[[char, freq] for char, freq in frequency_table.items()],
          colLabels=['Buchstabe', 'Häufigkeit'],
          loc='center')
#
#Huffman Baum erstellen und anzeigen
ax1 = fig.add_subplot(121, projection='3d')
root = generate_huffman_tree()


plot_huffman_tree(root, ax=ax1)
plt.show()
