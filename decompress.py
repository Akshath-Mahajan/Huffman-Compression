from custom_nodes import node

def read_file(filename):
    
    fh = open(filename, 'rb')
    non_bin_data = fh.readline()
    lengthofbits = eval(non_bin_data)
    non_bin_data = fh.readline()
    mapping = eval(non_bin_data.decode('utf-8'))
    bin_data_read = fh.read()
    temp = [bin(t)[2:].rjust(8, '0') for t in list(bin_data_read)]
    lengthofreadbits = 0
    for i in temp:
        lengthofreadbits+=len(i)
    extra_zeros = lengthofreadbits - lengthofbits
    temp[-1] = temp[-1][extra_zeros:]
    
    return mapping, ''.join(temp)
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
    print("Done decoding")
    return result


'''
def get_rev_sorted_keys(dictionary):
    temp = list(dictionary.keys())
    temp.sort(key=len, reverse=True)
    print(temp)
    return temp
def huffmanDecode (dictionary, text):
    rev_keys = get_rev_sorted_keys(dictionary)  #Biggest key should be matched first.
    res = ""
    while text:
        for k in rev_keys:
            if text.startswith(k):
                res += dictionary[k]
                text = text[len(k)+1:]
    return res
'''

def decompress(filename):
    m, s = read_file(filename)
    r = generate_tree(m)
    output = decode(s,r)
    fh = open(filename[:filename.index('.')]+".txt", 'w')
    fh.write(output)
    fh.close()
    node.clean_all()