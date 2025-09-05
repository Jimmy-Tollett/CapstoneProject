import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Tests {

    public boolean checkAsterixLength(byte[] message) {
        // Verify that the ASTERIX message length field matches the actual length
        if (message.length < 3) {
            throw new IllegalArgumentException("Message too short to contain header");
        }
        int declaredLen = ((message[1] & 0xFF) << 8) | (message[2] & 0xFF);
        int actualLen = message.length;
        return declaredLen == actualLen;
    }
    }

    /**
     * Test that a valid ASTERIX message passes the length check.
     * The message is a real example with the declared length matching the actual length.
     */
    @Test
    public void testValidMessage() {
        // Example ASTERIX message in hex (same as Python test)
        String hexStr = "15 00 3b c3 1b 7b 6b c1 81 00 00 00 01 00 0c 3d 56 bb dd 19 af fb a3 ad ce 7a fe 12 7a fe 12 17 44 51 f5 14 12 03 f3 05 78 40 7f f6 08 df 51 c7 7a fe 13 04 13 33 db 98";
        byte[] message = hexStringToByteArray(hexStr.replace(" ", ""));
        assertTrue(checkAsterixLength(message));
    }

    /**
     * Test that an invalid ASTERIX message fails the length check.
     * The message is missing a byte, so the declared length does not match the actual length.
     */
    @Test
    public void testInvalidMessage() {
        // Remove a byte to make the length invalid
        String hexStr = "15 00 3b c3 1b 7b 6b c1 81 00 00 00 01 00 0c 3d 56 bb dd 19 af fb a3 ad ce 7a fe 12 7a fe 12 17 44 51 f5 14 12 03 f3 05 78 40 7f f6 08 df 51 c7 7a fe 13 04 13 33 db";
        byte[] message = hexStringToByteArray(hexStr.replace(" ", ""));
        assertFalse(checkAsterixLength(message));
    }

    // Helper to convert hex string to byte array
    public static byte[] hexStringToByteArray(String s) {
        int len = s.length();
        byte[] data = new byte[len / 2];
        for (int i = 0; i < len; i += 2) {
            data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4)
                                 + Character.digit(s.charAt(i+1), 16));
        }
        return data;
    }
}