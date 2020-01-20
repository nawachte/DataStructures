#
#Name: Nicholas Wachter
#Student ID: 016170774
#Date (last modified): 5/14/19
#
# Lab 11
# Section 12
# Purpose of Lab: encode a text document with a huffman tree

import sys
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __lt__(self,other):
        return comes_before(self, other)

#node node -> bool
#if a is less than b return true else return false
def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq < b.freq:
        return True
    elif a.freq > b.freq:
        return False
    else:
        if a.char < b.char:
            return True
        return False


def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""

#str -> list
#open file, travers though each character and keep a counter for each character
def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    file = open(filename,'r')
    charList = [0]*256
    for line in file:
        for char in line:
            charList[ord(char)] += 1
    file.close()
    return charList

#list -> node
# create a huff tree with the char freq list by combining the first two and adding them back to the list
def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""

    ###make node list###
    nodeList = []
    for i in range(len(char_freq)):
        if char_freq[i] != 0:
            nodeList.append(HuffmanNode(i,char_freq[i]))
    ###sort node list###
    nodeList.sort()
    ###make tree###
    while len(nodeList)>1:
        ###make nodes###
        parent = HuffmanNode(None,None)
        nodeA = nodeList[0]
        nodeB = nodeList[1]
        #if comes_before(nodeA,nodeB) == True:
        parent.left = nodeA
        parent.right = nodeB
        parent.char = min(nodeA.char,nodeB.char)
        parent.freq = nodeA.freq + nodeB.freq
        #else:
            #pass
            # parent.left = nodeB
            # parent.right = nodeA
            # parent.char = min(nodeA.char,nodeB.char)
            # parent.freq = nodeA.freq + nodeB.freq
        ###add nodes back to list###
        nodeList.remove(nodeA)
        nodeList.remove(nodeB)
        nodeList.append(parent)
        nodeList.sort()
    return nodeList[0]

#node -> list
#make the 1 and 0 for each character by traversing the list for the leaves
def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    codeArray = ['']*256
    binString = ''
    tupleList = create_code_help(node,binString)
    for item in tupleList:
        codeArray[item[0]] = item[1]
    return codeArray

#node str -> list
#take the node and character string from the create code and traverse the tree
def create_code_help(node, binString):
    nodeList = []
    performedLeft = False
    if node.left is not None:
        binString += '0'
        nodeList += create_code_help(node.left, binString)
        performedLeft = True
    if node.right is not None:
        if performedLeft == True:
            binString = binString[:-1]
        binString += '1'
        nodeList += create_code_help(node.right, binString)
    if node.left is None and node.right is None:
        nodeList.append((node.char,binString))
    return nodeList

#list -> str
#use the list of character frequencies and make the header
def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    headerString = ''
    for i in range(256):
        if freqs[i] != 0:
            headerString += str(i)+' '+str(freqs[i])+' '
    if headerString[-1] == ' ':
        headerString = headerString[:-1]
    return headerString

#str str -> None
#use all of the functions to take a normal file and make a new, encoded file
def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    char_freq = cnt_freq(in_file)
    outFile = open(out_file, 'w', newline='')
    if char_freq == [0] * 256:
        outFile.close()
    else:
        huffNode = create_huff_tree(char_freq)
        codeArray = create_code(huffNode)
        header = create_header(char_freq)
        outFile.write(header)
        outFile.write("\n")
        inFile = open(in_file,'r')
        for line in inFile:
            for char in line:
                outFile.write(codeArray[ord(char)])
        outFile.close()
        inFile.close()
