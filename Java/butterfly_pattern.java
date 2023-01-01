
// Butterfly Pattern
public class ButterflyPattern {
    public static void main(String[] args) {
        int rows = 5;
        for (int i = 1; i <= rows; i++) {
            System.out.println("*".repeat(i) + " ".repeat(2 * (rows - i)) + "*".repeat(i));
        }
        for (int i = rows; i >= 1; i--) {
            System.out.println("*".repeat(i) + " ".repeat(2 * (rows - i)) + "*".repeat(i));
        }
    }
}
