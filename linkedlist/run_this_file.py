# add necessary directories to import
import sys;
#inserting at the end using linkedlist in python (change your import directory)
# IMPORTANT : Change your import directory else this will not work

# sys.path.append('/home/ubuntu/workspace/linkedlist/insert_at_end/insert_at_end_core');
# from insertion_at_end import insert_at_end;
# testLinkedlist = insert_at_end();
# testLinkedlist.add("sample element 1");
# testLinkedlist.add("sample element 2");
# testLinkedlist.add("sample element 3");
# testLinkedlist.add("sample element 4");
# testLinkedlist.add("sample element 5");
# testLinkedlist.printLinkedList();

# sys.path.append('/home/ubuntu/workspace/linkedlist/insert_after_an_element/insert_after_an_element_core');
# from insert_after_an_element import insert_after_an_element_class
# testLinkedList = insert_after_an_element_class();
# testLinkedList.add("Sample Data 1")
# testLinkedList.add("Sample Data 2")
# testLinkedList.add("Sample Data 3")
# testLinkedList.add("Sample Data 4")
# testLinkedList.printLinkedList();
# testLinkedList.addElementAfterAnElement('Sample Data 2', 'added data')
# testLinkedList.printLinkedList();

sys.path.append('/home/ubuntu/workspace/linkedlist/insert_before_an_element/insert_before_an_element_core');
from insert_before_an_element import insert_before_an_element_class
testLinkedList = insert_before_an_element_class();
testLinkedList.add("Sample Data 1")
testLinkedList.add("Sample Data 2")
testLinkedList.add("Sample Data 3")
testLinkedList.add("Sample Data 4")
testLinkedList.printLinkedList();
testLinkedList.addBefore('Sample Data 2', 'added data')
testLinkedList.printLinkedList();