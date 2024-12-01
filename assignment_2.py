import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LoginTest {

    private final Login login = new Login();

    @Test
    public void testInValidLogin() {
        System.out.println("Running testInValidLogin..."); // Added print statement
        assertFalse(login.validate("umairlatif@example.com", "password456"), "InValid login should return false.");
    }

    @Test
    public void testInvalidEmail() {
        System.out.println("Running testInvalidEmail..."); // Added print statement
        assertFalse(login.validate("invalid@example.com", "password123"), "Invalid email should return false.");
    }

    @Test
    public void testIncorrectPassword() {
        System.out.println("Running testIncorrectPassword..."); // Added print statement
        assertFalse(login.validate("johndoe@example.com", "wrong password"), "Incorrect password should return false.");
    }

    @Test
    public void testEmptyFields() {
        System.out.println("Running testEmptyFields..."); // Added print statement
        assertFalse(login.validate("", ""), "Empty fields should return false.");
    }

    @Test
    public void testSQLInjection() {
        System.out.println("Running testSQLInjection..."); // Added print statement
        assertFalse(login.validate("' OR 1=1 --", "password123"), "SQL injection attempt should return false.");
    }
}
