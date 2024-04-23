import pytest
from toolshop.base import Tool, Documentation, Parameter


def test_tool_name():
    class Hammer(Tool):
        def call(self):
            """Hammers a nail.
            Args:
                nail (str): Name of the nail to hammer.
            """
            pass

    h = Hammer()

    assert h.__name__ == 'hammer'
    

def test_noop_when_state_missing():
    class Hammer(Tool):

        def call(self, nail):
            """Hammers a nail.
            Args:
                nail (str): Name of the nail to hammer.
            """
            
            # When state is not provided, Tool should provide a no-op state object
            # and this will not raise an error. If state is provided, the tool
            # attempts to access the attribute ("non_existent_method") and therefore
            # should raise an AttributeError.    
            self.state.non_existent_method()
            self.latest_nail = nail
    
    Hammer()('Ned')

    with pytest.raises(AttributeError):
        Hammer(state=[1,2,3])('Ned')
