from app import greeting


def test_greeting():
    assert greeting("Melanie") == "Hello Melanie"
