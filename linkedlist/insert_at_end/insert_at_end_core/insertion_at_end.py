# add necessary directories to import
import sys;
sys.path.append('/home/ubuntu/workspace/linkedlist/insert_at_end');

#import node class
from Node.Node_Core import Node

class insert_at_end:
    def __init__(self):
        print("#created empty linked list")
        self.head = None;
        self.tail = None;
