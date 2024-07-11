import os
import pytest
import tempfile
from toolshop.agent.agent import Agent

class TestBasicFileSystemReasoning:
    @pytest.fixture
    def basic_file(self, tmpdir):
        # Create a temporary file for testing
        with tempfile.NamedTemporaryFile(dir=tmpdir, delete=False) as tmpfile:
            tmpfile.write(b"abc\n123\n")
        
        yield tmpfile.name
        
        os.remove(tmpfile.name)        

    def test_setup_file_fixture(self, basic_file):
        with open(basic_file, 'r') as file:
            contents = file.readlines()

        assert contents == ["abc\n", "123\n"]

    def test_insert_a_line_to_a_file(self, basic_file):
        app = Agent(False)
        app.do(f"Insert a new line 'hello world' in the file {basic_file} between the lines saying 'abc' and the line saying '123'.")

        with open(basic_file, 'r') as file:
            contents = file.readlines()
        
        assert contents == ["abc\n", "hello world\n", "123\n"]

    def test_replace_a_line_in_a_file(self, basic_file):
        app = Agent(False)
        app.do(f"Replace the line 'abc' in the file {basic_file} with the line 'hello world'.")

        with open(basic_file, 'r') as file:
            contents = file.readlines()
            
        assert contents == ["hello world\n", "123\n"]

