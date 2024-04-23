import pytest
from toolshop.file import (
    ReadFile, 
    CreateFile, 
    InsertLines, 
    DeleteLines, 
    ReplaceLines, 
    ReadDirectory,
    make_file_tools
)
import tempfile
import os


# Test Read
def test_read_basic(test_file):
    content = ReadFile()(test_file, include_line_numbers=False)
    assert content == "Line 1\nLine 2\nLine 3\n"


def test_read_with_line_numbers(test_file):
    content = ReadFile()(test_file, include_line_numbers=True)
    assert content == "1   |Line 1\n2   |Line 2\n3   |Line 3\n"


def test_read_start_and_end_line(test_file):
    content = ReadFile()(test_file, start_line=2, end_line=3, include_line_numbers=False)
    assert content == "Line 2\nLine 3\n"


def test_read_non_existing_file():
    with pytest.raises(FileNotFoundError):
        ReadFile()("/tmp/non_existing_file.txt")


# Test CreateFile
def test_create_file():  
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'new_file.txt')
        content = "This is a test file.\n"
        CreateFile()(file_path, content)

        assert os.path.exists(file_path)

        file_content = ReadFile()(file_path, include_line_numbers=False)    
        assert file_content == content


# Test InsertLines
def test_insert_lines_middle(test_file):
    ReadFile()(test_file)
    InsertLines()(test_file, 'Inserted Line\n', 2)
    updated_content = ReadFile()(test_file, include_line_numbers=False)
    assert 'Inserted Line' == updated_content.splitlines()[1]

def test_insert_lines_end(test_file):
    ReadFile()(test_file)
    InsertLines()(test_file, 'End Line\n', -1)
    updated_content = ReadFile()(test_file, include_line_numbers=False)
    assert 'End Line' == updated_content.splitlines()[-1]


# Test DeleteLines
def test_delete_single_line(test_file):
    original_content = ReadFile()(test_file)
    DeleteLines()(test_file, 2, 2)
    updated_content = ReadFile()(test_file, include_line_numbers=False)
    assert len(original_content.splitlines()) - 1 == len(updated_content.splitlines())
    assert updated_content.splitlines()[1] == 'Line 3'


def test_delete_line_range(test_file):
    original_content = ReadFile()(test_file)
    DeleteLines()(test_file, 1, 2)
    updated_content = ReadFile()(test_file, include_line_numbers=False)
    assert len(updated_content.splitlines()) == len(original_content.splitlines()) - 2
    assert updated_content.splitlines()[0] == 'Line 3'


# Test ReplaceLines
def test_replace_single_line(test_file):
    ReadFile()(test_file, include_line_numbers=False)
    ReplaceLines()(test_file, 'Replaced Line\n', 2, 2)
    updated_content = ReadFile()(test_file, include_line_numbers=False)
    assert 'Replaced Line' == updated_content.splitlines()[1]


def test_replace_line_range(test_file):
    ReadFile()(test_file, include_line_numbers=False)
    ReplaceLines()(test_file, 'New Line 1\nNew Line 2\n', 1, 2)
    updated_content = ReadFile()(test_file, include_line_numbers=False)
    assert updated_content.splitlines()[0] == 'New Line 1' 
    assert updated_content.splitlines()[1] == 'New Line 2'


def test_replace_edge_cases(test_file):
    original_content = ReadFile()(test_file)
    # Replace first line
    ReplaceLines()(test_file, 'First Line replaced\n', 1, 1)
    updated_first = ReadFile()(test_file, include_line_numbers=False)
    assert 'First Line replaced' == updated_first.splitlines()[0]
    # Replace last line
    last_line_number = len(original_content.splitlines())
    ReplaceLines()(test_file, 'Last Line replaced\n', last_line_number, last_line_number)
    updated_last = ReadFile()(test_file, include_line_numbers=False)
    assert 'Last Line replaced' == updated_last.splitlines()[-1]


def test_get_file_tool_set(test_file):
    tools = make_file_tools()

    read_file = [t for t in tools if t.__name__ == 'read_file'][0]
    delete_lines = [t for t in tools if t.__name__ == 'delete_lines'][0]

    with pytest.raises(ValueError):
        delete_lines(test_file, 2, 2)
    
    read_file(test_file)
    delete_lines(test_file, 2, 2)

    with open(test_file) as f:
        assert f.read() == "Line 1\nLine 3\n"


def test_read_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Set up directory and files
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'subdir', 'file2.txt')
        with open(file1_path, 'w') as f:
            f.write('Hello')
        with open(file2_path, 'w') as f:
            f.write('World')

        # Test RepoContext
        output = ReadDirectory()(temp_dir)
        expected_output = ("===== File: " + file1_path + " =====\n1   |Hello\n\n"
                           "===== File: " + file2_path + " =====\n1   |World\n\n")
        assert output == expected_output


def test_read_directory_on_toolshop():
    # get the root of this package
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    output = ReadDirectory()(root)
    print(output)

