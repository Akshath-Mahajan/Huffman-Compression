from custom_nodes import node

def to_bytes(data):
  b = bytearray()
  for i in range(0, len(data), 8):
    b.append(int(data[i:i+8], 2))
  return bytes(b) 

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
    return char_freq

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
        
def generate_nodes(freq_table):
    nodes = []
    for i in freq_table.keys():
        temp = node(None, None, i, None, freq_table[i])
                    

def compress(filename):
    ft = get_freq_dict(filename)
    generate_nodes(ft)
    t = Huffman_Tree(node.COMPONENTS)   #t is now the root of huffman tree
    t.generate_bits()   
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
    f.write(to_bytes(t))
    f.close()
    node.clean_all()
