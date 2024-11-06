import heapq
import collections
from bitarray import bitarray
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
from docx import Document

class FileReader:
    """Class to handle reading text from different file formats."""

    @staticmethod
    def read(file_path):
        if file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        elif file_path.endswith('.pdf'):
            pdf_reader = PdfReader(file_path)
            text = ''.join(page.extract_text() for page in pdf_reader.pages if page.extract_text())
            return text
        elif file_path.endswith('.html'):
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')
                return soup.get_text()
        elif file_path.endswith('.docx'):
            doc = Document(file_path)
            text = '\n'.join(para.text for para in doc.paragraphs)
            return text
        else:
            raise ValueError("Unsupported file format")


class HuffmanNode:
    """Class representing a node in the Huffman Tree."""
    
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None
    
    # For priority queue ordering
    def __lt__(self, other):
        return self.frequency < other.frequency


class HuffmanCoding:
    """Class to perform Huffman encoding on text data."""

    def __init__(self, data):
        self.data = data
        self.frequency = self.calculate_frequency(data)
        self.huffman_tree = self.build_huffman_tree()
        self.encoding_map = self.create_encoding_map()

    def calculate_frequency(self, data):
        return collections.Counter(data)

    def build_huffman_tree(self):
        heap = [HuffmanNode(symbol, freq) for symbol, freq in self.frequency.items()]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = HuffmanNode(None, left.frequency + right.frequency)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)
        
        return heap[0] if heap else None

    def create_encoding_map(self):
        encoding_map = {}
        self._generate_codes(self.huffman_tree, '', encoding_map)
        return encoding_map

    def _generate_codes(self, node, current_code, encoding_map):
        if node:
            if node.symbol is not None:  # It's a leaf node
                encoding_map[node.symbol] = current_code
            self._generate_codes(node.left, current_code + '0', encoding_map)
            self._generate_codes(node.right, current_code + '1', encoding_map)

    def encode(self):
        return bitarray(''.join(self.encoding_map[char] for char in self.data))


class Compressor:
    """Class to manage compression and calculate compression ratio."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = FileReader.read(file_path)
        self.huffman_coding = HuffmanCoding(self.data)
        self.encoded_data = self.huffman_coding.encode()

    def calculate_compression_ratio(self):
        original_size = len(self.data.encode('utf-8')) * 8  # original size in bits
        compressed_size = len(self.encoded_data)            # compressed size in bits
        return (1 - (compressed_size / original_size)) * 100

    def compress(self):
        compression_ratio = self.calculate_compression_ratio()
        print(f"Original size (bits): {len(self.data.encode('utf-8')) * 8}")
        print(f"Compressed size (bits): {len(self.encoded_data)}")
        print(f"Compression ratio: {compression_ratio:.2f}%")
        return self.huffman_coding.encoding_map, self.encoded_data, compression_ratio



file_paths = ['sample.txt', 'sample.html', 'sample.pdf', 'sample.docx'] 
for file_path in file_paths:
    compressor = Compressor(file_path)
    compressor.compress()
