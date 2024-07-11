import pytest
import os

def is_running_in_containerized_environment():
    """Check if currently running inside a Docker container."""
    if os.getenv("IS_RUNNING_IN_CONTAINERIZED_ENVIRONEMENT") == "1":
        return True
    else:
        return False

def pytest_runtest_setup(item):
    """Skip tests marked with @pytest.mark.require_containerized_environment if not in Docker."""
    if "require_containerized_environment" in item.keywords and not is_running_in_containerized_environment():
        pytest.skip("This test is only allowed to run in a containerized Docker environment")
