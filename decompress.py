from custom_nodes import node
def read_file(filename):
    fh = open(filename, 'rb')
    non_bin_data = fh.readline()
    lengthofbits = eval(non_bin_data)
    non_bin_data = fh.readline()
    mapping = eval(non_bin_data.decode('utf-8'))
    i = 0
    bin_data = ""
    while True:
        try:
            bin_data += str(bin(ord(fh.read(1)))[2:].rjust(8, '0'))
        except TypeError: #ord cannot accept str of len 0
            break
    extra_zeros = len(bin_data) - lengthofbits
    bin_data = bin_data[0:-8] + bin_data[-8+extra_zeros:]

    
    return mapping,bin_data

def generate_tree(mapping):
    '''
    INPUT: DICTIONARY OF MAPPING
    GOAL: GENERATE TREE OBJECT FROM THE MAPPING
    RETURN: ROOT OF TREE
    '''
    ROOT = node(None, None, "ROOT", None, 0)
    current = ROOT
    for k,v in mapping.items():
        for char in v:
            if char == '0':
                if current.left_child != None:
                    current = current.left_child
                else:
                    TEMP = node(None, None, "", None, 0)
                    current.set_left_child(TEMP)
                    current = TEMP
            if char == '1':
                if current.right_child != None:
                    current = current.right_child
                else:
                    TEMP = node(None, None, "", None, 0)
                    current.set_right_child(TEMP)
                    current = TEMP
        current.set_name(k)
        current = ROOT
        
    return ROOT

def decode(sequence, root):
    result = ""
    current = root
    for i in sequence:
        if i == '0':
            if current.left_child != None:
                current = current.left_child
                if current.left_child == None and current.right_child == None:
                    result+=current.name
                    current = root
            
        if i == '1':
            if current.right_child != None:
                current = current.right_child
                if current.left_child == None and current.right_child == None:
                    result+=current.name
                    current = root
    return result

def decompress(filename):
    m, s = read_file(filename)
    r = generate_tree(m)
    output = decode(s,r)
    fh = open(filename[:-3]+"txt", 'w')
    fh.write(output)
    fh.close()

        
        

decompress('Tests/bible.bin')