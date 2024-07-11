from toolshop.tools.terminal import Shell, PythonExec


def test_smoke():
    Shell()("ls")
    PythonExec()("x = 1+1", ['x'])


def test_python_exec():
    vars = PythonExec()("x = 1+1\ny = 2+2", ['x', 'y'])

    assert vars['x'] == 2
    assert vars['y'] == 4


def test_shell():
    output = Shell()("echo hi")

    assert output[:2] == 'hi'
