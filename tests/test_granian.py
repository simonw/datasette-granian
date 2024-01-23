from datasette_test import wait_until_responds
import httpx
import pytest
from subprocess import Popen, PIPE
import sys


@pytest.fixture(scope="session")
def server():
    process = Popen(
        [
            sys.executable,
            "-m",
            "datasette",
            "granian",
            "--port",
            "8126",
            "--memory",
        ],
        stdout=PIPE,
    )
    wait_until_responds("http://localhost:8126/")
    yield "http://localhost:8126"
    process.terminate()
    process.wait()


def test_granian(server):
    response = httpx.get(server + "/-/versions.json")
    assert response.status_code == 200
    info = response.json()
    assert "python" in info
    assert "datasette" in info
