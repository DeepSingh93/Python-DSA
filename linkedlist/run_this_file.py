# add necessary directories to import
import sys;
#inserting at the end using linkedlist in python (change your import directory)
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/linkedlist/insert_at_end/insert_at_end_core');
from insertion_at_end import insert_at_end;
testLinkedlist = insert_at_end();
testLinkedlist.add("sample element 1");
testLinkedlist.add("sample element 2");
testLinkedlist.add("sample element 3");
testLinkedlist.add("sample element 4");
testLinkedlist.add("sample element 5");
testLinkedlist.printLinkedList();