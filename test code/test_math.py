from maths import APP
import pytest
from fastapi.testclient import TestClient

Client=TestClient(APP)

def test_read_root():
    response = Client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_fibonacci_is_define_or_not():
    response = Client.get("/factorial/{length}")
    assert response.status_code == 404

def test_fibonacci_length_is_zero():
    response = Client.get("/fibonacci/{length}")
    assert response.status_code == 400

def test_fibonacci_length_is_char():
    response = Client.get("/fibonacci/{length}")
    assert response.status_code == 400

def test_fibonacci_length_is_negative():
    response = Client.get("/fibonacci/{length}")
    assert response.status_code == 400
    
def test_fectorial_is_define_or_not():
    response = Client.get("/factorial/{number}")
    assert response.status_code == 404

def test_factorial_no_is_zero():
    response = Client.get("/factorial/{number}")
    assert response.status_code == 400

def test_fibonacci_no_is_char():
    response = Client.get("/factorial/{number}")
    assert response.status_code == 400

def test_factorial_no_is_negative():
    response = Client.get("/factorial/{number}")
    assert response.status_code == 400