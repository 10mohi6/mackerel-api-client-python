import os
import time

import pytest
from mackerel.api import Client


@pytest.fixture(scope="module", autouse=True)
def scope_module():
    url = os.environ["MACKEREL_API_KEY"]
    yield Client(url)


@pytest.fixture(scope="function", autouse=True)
def client(scope_module):
    time.sleep(1)
    yield scope_module


# @pytest.mark.skip
def test_api_get(client):
    expected = 200
    actual = client.get("/org").status_code
    assert expected == actual


# @pytest.mark.skip
def test_api_post(client):
    expected = 200
    data = {"name": "ExampleAlert", "memo": "This is an alert example."}
    actual = client.post("/alert-group-settings", data).status_code
    assert expected == actual


# @pytest.mark.skip
def test_api_put(client):
    expected = 200
    id = client.get("/alert-group-settings").json()["alertGroupSettings"][0]["id"]
    data = {"name": "ExampleAlert", "memo": "This is an alert example!"}
    actual = client.put("/alert-group-settings/{}".format(id), data).status_code
    assert expected == actual


# @pytest.mark.skip
def test_api_delete(client):
    expected = 200
    id = client.get("/alert-group-settings").json()["alertGroupSettings"][0]["id"]
    actual = client.delete("/alert-group-settings/{}".format(id)).status_code
    assert expected == actual
