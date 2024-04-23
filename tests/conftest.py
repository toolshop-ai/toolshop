import pytest
from tempfile import NamedTemporaryFile
import os

@pytest.fixture(scope="function")
def test_file():
    with NamedTemporaryFile(mode='w+', delete=False) as tmp:
        tmp.write("Line 1\nLine 2\nLine 3\n")
        tmp_path = tmp.name
    
    yield tmp_path
    os.remove(tmp_path)
