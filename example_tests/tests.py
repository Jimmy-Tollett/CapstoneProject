def check_asterix_length(message: bytes) -> bool:
    """
    Verify that the ASTERIX message length field matches the actual length.
    
    Parameters:
        message (bytes): Full ASTERIX message (starting with category).
    
    Returns:
        bool: True if lengths match, False otherwise.
    """
    if len(message) < 3:
        raise ValueError("Message too short to contain header")
    
    # Category = message[0]
    declared_len = int.from_bytes(message[1:3], byteorder="big")
    actual_len = len(message)

    print(f"Declared length: {declared_len}, Actual length: {actual_len}")
    return declared_len == actual_len


def test_valid_message():
    hex_str = "15 00 3b c3 1b 7b 6b c1 81 00 00 00 01 00 0c 3d 56 bb dd 19 af fb a3 ad ce 7a fe 12 7a fe 12 17 44 51 f5 14 12 03 f3 05 78 40 7f f6 08 df 51 c7 7a fe 13 04 13 33 db 98"
    message_bytes = bytes.fromhex(hex_str)
    assert check_asterix_length(message_bytes) is True


def test_invalid_message():
    hex_str = "15 00 3b c3 1b 7b 6b c1 81 00 00 00 01 00 0c 3d 56 bb dd 19 af fb a3 ad ce 7a fe 12 7a fe 12 17 44 51 f5 14 12 03 f3 05 78 40 7f f6 08 df 51 c7 7a fe 13 04 13 33 db 98"
    message_bytes = bytes.fromhex(hex_str)
    assert check_asterix_length(message_bytes) is False
