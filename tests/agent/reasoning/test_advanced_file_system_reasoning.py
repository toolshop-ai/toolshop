import os
import pytest
import tempfile
from toolshop.agent.agent import Agent
from ..helpers import get_fixme_file, get_object

class TestDoublyLinkedList:
    @pytest.fixture
    def fixme_file(self, tmpdir):
        # Get contents of file to fix
        with open(get_fixme_file('doubly_linked_list_broken.py'), 'r') as file:
            contents = file.read().encode('utf-8')

        # Copy contents to a temporary file
        with tempfile.NamedTemporaryFile(dir=tmpdir, delete=False) as tmpfile:
            tmpfile.write(contents)

        yield tmpfile.name
        
        os.remove(tmpfile.name)  
    
    def test_fixture(self, fixme_file):
        with open(fixme_file, 'r') as file:
            contents = file.readlines()

        assert contents[0] == "class DoublyLinkedListNode:\n"

    def test_class_definition_from_path(self):
        path = get_fixme_file('doubly_linked_list_broken.py') 

        DoublyLinkedListNode = get_object('DoublyLinkedListNode', path)
        DoublyLinkedListNode()

    @pytest.mark.require_containerized_environment
    def test_require_containerized_environment(self):
        assert True

    @pytest.mark.require_containerized_environment
    def test_fix_doubly_linked_list(self, fixme_file):
        app = Agent(False)
        
        app.do(f"Fix the DoublyLinkedListNode class in '{fixme_file}'. Keep the class signature the same.")
        
        print("\n=== start of modified file (from test_fix_doubly_linked_list)  ===")
        with open(fixme_file, 'r') as file:
            print(file.read())
        print("\n=== end of modified file (from test_fix_doubly_linked_list)  ===")

        DoublyLinkedListNode = get_object('DoublyLinkedListNode', path=fixme_file)
        node1 = DoublyLinkedListNode()
        node2 = DoublyLinkedListNode()
        
        node1.insert_after(node2)
        assert node1.next == node2
        assert node2.prev == node1
        assert node2.next is None
        assert node1.prev is None
        assert node1.next.prev == node1
        assert node2.prev.next == node2
        print('All tests passed.')



class TestMergeSort:
    @pytest.fixture
    def fixme_file(self, tmpdir):
        # Get contents of file to fix
        with open(get_fixme_file('merge_sort_broken.py'), 'r') as file:
            contents = file.read().encode('utf-8')

        # Copy contents to a temporary file
        with tempfile.NamedTemporaryFile(dir=tmpdir, delete=False) as tmpfile:
            tmpfile.write(contents)

        yield tmpfile.name
        
        os.remove(tmpfile.name)  
    
    def test_fixture(self, fixme_file):
        with open(fixme_file, 'r') as file:
            contents = file.readlines()

        assert contents[0] == "def merge_sort(l: list[int]):\n"

    @pytest.mark.require_containerized_environment
    def test_fix_merge_sort(self, fixme_file):
        app = Agent(False)
        
        app.do(f"Fix the merge_sort function in '{fixme_file}'. Keep the function signatures the same.")
        
        print("\n=== start of modified file (from test_fix_doubly_linked_list)  ===")
        with open(fixme_file, 'r') as file:
            print(file.read())
        print("\n=== end of modified file (from test_fix_doubly_linked_list)  ===")

        merge_sort = get_object('merge_sort', path=fixme_file)
 
        x = [1,5,2,4,3,3]
        assert merge_sort(x) == [1,2,3,3,4,5]

        print('All tests passed.')

