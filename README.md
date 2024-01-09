
# Huffman Code Visualization

This Python repository includes scripts for visualizing the Huffman coding algorithm using Matplotlib. The Huffman coding algorithm is a widely used method for lossless data compression.

## Table of Contents

- [Overview](#overview)
- [Challenge](#challenge)
- [Visual Huffman Coding Process](#visual-huffman-coding-process)
- [Visualization Approach](#visualization-approach)
- [Usage](#usage)
- [Example](#example)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

The repository consists of a Python script that demonstrates & visualizes the Huffman coding algorithm. It visualizes the Huffman tree (3D) , frequency tables, and encoding of text using Huffman coding.

## Challenge

Our challenge here is to create a three-dimensional visualization of Huffman coding. We aim to showcase it using a selected binary example. The goal is to graphically illustrate the process of Huffman coding to demonstrate efficient data compression and the functionality of the algorithm.

## Visual Huffman Coding Process

1. **Frequency Analysis:** Begin by analyzing the frequency of individual characters in the given Text.
2. **Building the Huffman Tree:** Select the two least frequent characters and combine then into a node, with the sum of their frequencies becoming the value of the new node. Repeat this process until all characters are merged into a single binary tree.
3. **Assigning Binary Codes:** Traverse the tree to assign a binary code to each leaf (original character). Assign '0' to each left path and '1' to each right path. This coding results in the Huffman Coding, where shorter codes represent more frequent characters and longer codes represent rarer characters. This knowledge is then used to create the new "encoded data word".

## Visualization Approach

For the visualization, we'll use Python and the matplotlib package to represent the Huffman tree in three dimensions. Here's a breakdown of the steps:

1. **Frequency Analysis:** Determine the frequency of characters (in our case, letters) in the given text, creating a table that illustrates these frequencies.
2. **Building the Huffman Tree:** Construct the Huffman tree from the frequency table.
3. **Three-Dimensional Visualization:** Utilize matplotlib to visualize the tree in a three-dimensional space, representing characters in the leaf nodes. The tree will have multiple levels, with characters of higher frequency positioned higher in the tree.
4. **Traversal and Coding:** To read the coding, traverse the tree. Since we encode in binary, label each left edge of a node with '0' and each right edge with '1'. The encoding of each character in our example word will be demonstrated by traversing the tree from the top node to the leaf node containing the respective character.

This visualization aims to make the process of Huffman coding understandable by demonstrating how the traversal of the tree results in the encoding of individual characters in a given text.


## Usage

1. **Run the Code:** Clone this repository and execute the `Huffman.py` script.
2. **Input Text:** Enter a text string when prompted to create a Huffman encoding visualization and display the encoded output.
3. **Visualizations:** The script generates visualizations of the Huffman tree, frequency tables, and encodings using Matplotlib.

## Example

![Example Image](huffman_tree.png)

## Getting Started

To run the code:

1. Clone this repository to your local machine.
2. Ensure you have Python installed (Python 3 recommended).
3. Install the required dependencies mentioned in the `Dependencies` section.
4. Run the `Multimedia.py` script.

## Dependencies

The following dependencies are required to run the scripts:
- Python (3.x recommended)
- Matplotlib

Install Matplotlib using pip:

```bash
pip3 install matplotlib
```

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to improve the code, add new features, or fix bugs.

## License

This project is licensed under the [MIT License](LICENSE).
