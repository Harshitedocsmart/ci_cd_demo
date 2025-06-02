from main import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.data == b"Hello from source-based Cloud Run!"
