def all_tools(framework='marvin'):
    from .terminal import Shell, PythonExec, Browse
    from .data import Sql, Histogram
    from .file import make_file_tools
    from .meta import EnableResultToFile
    from .base import State

    state = State()

    tools = [
        Shell(state=state),
        PythonExec(state=state),
        Browse(state=state),
        Sql(state=state),
        Histogram(state=state),
        EnableResultToFile(state=state),
        *make_file_tools(state=state),
    ]
    
    if framework == 'marvin':
        return [t.to_marvin() for t in tools]

