import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Tests {

    public boolean isValidMessage(String message, int declaredLength) {
        return message.length() == declaredLength;
    }

    @Test
    public void testValidMessage() {
        String message = "FLIGHT123";
        int declaredLength = 9;
        assertTrue(isValidMessage(message, declaredLength));
    }

    @Test
    public void testInvalidMessage() {
        String message = "FLIGHT123";
        int declaredLength = 8;
        assertFalse(isValidMessage(message, declaredLength));
    }
}