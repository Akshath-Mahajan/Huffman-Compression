from custom_nodes import node

def get_freq_dict(filename):
    fh = open(filename, 'r')
    all_text = fh.read()
    fh.close()
    char_freq = {}
    for char in all_text:
        try:
            char_freq[char]+=1
        except KeyError:
            char_freq[char] = 1
    
    # res = {k: v for k, v in sorted(char_freq.items(), key=lambda item: item[1])}
    return char_freq

def _to_Bytes(data):
  b = bytearray()
  for i in range(0, len(data), 8):
    b.append(int(data[i:i+8], 2))
  return bytes(b)
 
def Huffman_Tree(components): #COMPONENTS IS LIST OF OBJS, RETURNS ROOT ONLY
    if len(components) == 2:
        if components[0].freq < components[1].freq:
            components[0],components[1] = components[1], components[0]
        
        return components[0].merge(components[1])
    else:
        a = None
        b = None
        min1 = float('inf')
        min2 = float('inf')
        for node in components:
            if node.freq <= min1:
                a,b = node, a
                min1, min2 = node.freq, min1
            else:
                if node.freq < min2 and node.freq > min1:
                    b = node
                    min2 = node.freq
        b.merge(a)
        return Huffman_Tree(components)
        
def generate_nodes(filename):
    freq_table = get_freq_dict(filename)
    nodes = []
    for i in freq_table.keys():
        temp = node(None, None, i, None, freq_table[i])
    
def get_huffman_bits(filename):
    generate_nodes(filename)    #Generate node.components
    t = Huffman_Tree(node.COMPONENTS)   #t is now the root of huffman tree
    t.generate_bits()                   
    return node.NAME_TO_BITS

def compress(filename):
    get_huffman_bits(filename)
    fh = open(filename, 'r')
    l = fh.read()
    fh.close()
    chars = [x for x in l]
   
    for i in range(len(chars)):
        chars[i] = node.NAME_TO_BITS[chars[i]]
    t = ''.join(chars)
    temp = {k:v for k,v in node.NAME_TO_BITS.items() if len(k) <= 1}
    outputfile = filename[0: filename.index('.')] + '.bin'
    f = open(outputfile, 'w')
    f.write(str(len(t))+"\n")
    f.write(str(temp)+"\n")
    f.close()
    f = open(outputfile, 'ab')
    f.write(_to_Bytes(t))
    f.close()
    node.clean_all()
    #For test sake, test pickle and text dict storage.
compress('Tests/bible.txt')