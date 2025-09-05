def is_valid_message(message: str, declared_length: int) -> bool:
    """Check if the declared length matches the actual message length."""
    return len(message) == declared_length


def test_valid_message():
    message = "FLIGHT123"
    declared_length = 9
    assert is_valid_message(message, declared_length) is True


def test_invalid_message():
    message = "FLIGHT123"
    declared_length = 8
    assert is_valid_message(message, declared_length) is False