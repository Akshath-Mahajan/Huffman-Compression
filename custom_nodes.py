class node():
    NAME_TO_OBJ = {} #WILL ALWAYS CONTAIN ALL NODES, INCLUDING EMPTY MERGING NODES [NAMEOFNODE->OBJ]
    COMPONENTS = [] #WILL ALWAYS STORE ROOT OF A NODE [OBJECTS STORED, NOT NAME]
    NAME_TO_BITS = {} #NAME -> BINARY_SEQ
    def __init__(self, parent, left_child, name, right_child, f):
        self.parent = parent
        self.left_child = left_child
        self.name = name
        self.freq = f
        self.right_child = right_child
        self.binary_seq = ""

        node.NAME_TO_OBJ[str(name)] = self

        node.COMPONENTS.append(self)
        try:
            node.COMPONENTS.remove(left_child)
        except ValueError:
            pass
        try:
            node.COMPONENTS.remove(right_child)
        except ValueError:
            pass
        try:
            left_child.parent = self
        except AttributeError:
            pass
        try:
            right_child.parent = self
        except AttributeError:
            pass
    def __str__(self):
        return str(self.name)
    def __repr__(self):
        return str(self.name)
    def __lt__(self, other):
        return self.freq < other.freq
    def __gt__(self, other):
        return self.freq > other.freq
        
    def set_name(self, obj):
        self.name = obj
    def set_freq(self, obj):
        self.freq = obj
    def get_freq(self):
        return int(self.freq) 
    def get_root(self):
        if self.parent != None:
            return self.parent.get_root()
        return self
    
    def set_left_child(self, obj):
        try:
            obj = obj.get_root()
        except:
            pass
        try:
            node.COMPONENTS.remove(obj)
        except ValueError:
            pass
        self.left_child = obj
        obj.parent = self
    def set_right_child(self,obj):
        try:
            obj = obj.get_root()
        except:
            pass
        try:
            node.COMPONENTS.remove(obj)
        except ValueError:
            pass
        self.right_child = obj
        obj.parent = self

    def merge(self, other):
        lhs = self.get_root()
        rhs = other.get_root()
        MT = node(None, lhs, str(lhs)+str(rhs), rhs, lhs.get_freq()+rhs.get_freq())
        return MT

    # def get_depth(self):
        # i = 0
        # while self.parent != None:
        #     i+=1
        #     self = self.parent
        # return i
    def generate_bits(self):    #self needs to be a root
        try:
            self.left_child.binary_seq = self.binary_seq + "0"
        except AttributeError:
            pass
        try:
            self.right_child.binary_seq = self.binary_seq + "1"
        except AttributeError:
            pass
        try:
            self.left_child.generate_bits()
        except:
            pass
        try:
            self.right_child.generate_bits()
        except:
            pass
        if len(self.name) == 1:
            node.NAME_TO_BITS[str(self.name)] = self.binary_seq
            
    def clean_all():
        for k,v in node.NAME_TO_OBJ.items():
            del(v)
        node.COMPONENTS = []
        node.NAME_TO_BITS = {}
        node.NAME_TO_OBJ = {}
        