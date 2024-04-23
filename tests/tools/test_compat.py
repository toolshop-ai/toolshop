
from toolshop.base import Tool
from toolshop.logging import logger

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


def test_tool_langchain_compatibility():
    from langchain.agents.openai_assistant import OpenAIAssistantRunnable

    assistant = OpenAIAssistantRunnable.create_assistant(
        name="assistant",
        instructions="You hammer nails",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-turbo"
    )

    output = assistant.invoke({"content": "Hammer a nail named Ned."})

    print(output) 
