from test.unit.landingpage import client

def test_landing(client):
    landing = client.get()