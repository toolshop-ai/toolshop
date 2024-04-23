# Toolshop
The Tool Framework for AI Agents

# Usage
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
developing tools with Toolshop, your tools inherit many helpful features.
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
* __Compatibility__: Toolshop aims to be compatible with most major LLM frameworks. 
  Avoid framework lock-in and easily use the same tools with different frameworks.

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