import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    # Count the frequency of each character in the input data
    frequency = Counter(data)

    # Create a priority queue (min heap) for Huffman nodes
    priority_queue = [HuffmanNode(char=char, freq=freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    # Build the Huffman tree
    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)

        internal_node = HuffmanNode(freq=left_child.freq + right_child.freq)
        internal_node.left = left_child
        internal_node.right = right_child

        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]  # The root of the Huffman tree

def build_huffman_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}

    if root is not None:
        if root.char is not None:
            codes[root.char] = current_code
        build_huffman_codes(root.left, current_code + "0", codes)
        build_huffman_codes(root.right, current_code + "1", codes)

def huffman_encoding(data):
    if not data:
        return None, None

    root = build_huffman_tree(data)
    codes = {}
    build_huffman_codes(root, codes=codes)

    encoded_data = "".join(codes[char] for char in data)
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if not encoded_data or root is None:
        return None

    decoded_data = ""
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = root

    return decoded_data


# Example usage:
data = "huffman coding is fun"
encoded_data, huffman_tree = huffman_encoding(data)
decoded_data = huffman_decoding(encoded_data, huffman_tree)

print("Original data:", data)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)
