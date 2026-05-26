from copy import deepcopy
from pathlib import Path
import sys

from fastapi.testclient import TestClient
import pytest

# Ensure the repository root is importable when running tests or importing conftest directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.app import app as fastapi_app, activities as activities_data


@pytest.fixture(scope="function")
def app():
    return fastapi_app


@pytest.fixture(scope="function")
def client(app):
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = deepcopy(activities_data)
    yield
    activities_data.clear()
    activities_data.update(deepcopy(original_activities))
