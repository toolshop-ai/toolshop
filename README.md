# Toolshop
A Tool Framework for AI Agents


# Chat
Toolshop ships with a default chatbot equipped with all of Toolshop's tools.

To install and chat, run:
```
pip install toolshop
ts chat
```


# Usage

### Marvin
```
from toolshop import all_tools
from marvin.beta import Application

app = Application(
    tools=all_tools()
)

app.say("Write mergesort.py")
app.say("Test mergesort.py")
```


# Description
Toolshop is a general framework for developing tools used by LLM Agents. By
developing tools with Toolshop, your tools inherit several helpful features.
* __Configuration__: Toolshop tools are classes, not functions. This enables users
  to configure their tools for a particular session before passing them to the
  agent.
* __Confirmations__: Toolshop makes it easy to add required user confirmations
  to tool calls. Examples might include an agent editing sensitive files or
  provisioning cloud resources.
* __Constraints__: Tools can share state. This allows users to enforce constraints
  that require more context than the tool call arguments alone. Examples might
  include prevention of multiple parallel edits to the same file, requiring file
  reads before file edits, and cost-based limits on tool usage.


# Design Philosphy

### Design for AGI
Agents will continue to improve
[[ref](https://twitter.com/H0wie_Xu/status/1745657992459272423)]. Developers
should spend time building things that *benefit* from improved agents rather
than *suffer*. Tool development is a great example of work that directly
benefits from improved agents. The recent movement of AI companies away from simple
text-completion models and towards tool-assisted chat completion models reinforces
the importance of tool development
[[ref](https://platform.openai.com/docs/guides/text-generation/completions-api), [ref](https://docs.anthropic.com/claude/reference/complete_post)].


### Constrain tools, not process
Prompts that correct agent behavior by heavily constraining process may actually
hold back more intelligent agents that do not require such corrective
hand-holding. By instead enforcing constraints in the tools themselves, the
planning and reasoning process native to the underlying agent is unhindered. The
reasoning and planning capabilities of agentic AI offered by companies such as
OpenAI and Anthropic will continue to improve over time.


### Tools can share state
It is powerful to enforce required order-of-operations at the tool-level, 
rather than simply "encouraging" this at the prompt-level. Enforcing workflows at the
tool-level can guarantee tools are used appropriately. An example use 
case where a developer may wish to enforce tool-level rules
are ReadFile and WriteFile tools. Here, you may want require that files are 
always read (or re-read) before being written, so that the agent is always
aware of the latest contents in the file before writing. 

To assist in this pattern, Toolshop tools can share state to track. Toolshop 
currently supports a global State class which, once instantiated, can be 
injected into any tool via the `state` argument.
