import tempfile
import os

def write_tmp_file(contents):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(contents)

    return tmp_file.name

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def get_object(object_name, path):
    with open(path, 'r') as file:
        contents = file.read()
    
    scope = {}

    exec(contents, scope)

    return scope[object_name]
        
def get_tests_root():
    return os.path.dirname(os.path.abspath(__file__))

def get_fixme_file(filename):
    return os.path.join(get_tests_root(), 'fixme', filename)
