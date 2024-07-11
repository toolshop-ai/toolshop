
from toolshop.core.base import Tool
from toolshop.core.logging import logger

logger.setLevel("INFO")


class Hammer(Tool):
    def call(self, nail):
        """Hammers a nail.
        Args:
            nail (str): Name of the nail to hammer.
        """
        self.latest_nail = nail


def test_tool_marvin_compatibility():
    from marvin.beta import Application
    
    hammer = Hammer()

    app = Application(tools=[hammer])
    app.say("Hammer a nail named Ned.")

    assert hammer.latest_nail == "Ned"
