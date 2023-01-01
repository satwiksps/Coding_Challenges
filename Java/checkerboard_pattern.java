
// Checkerboard Pattern
public class CheckerboardPattern {
    public static void main(String[] args) {
        int rows = 8;
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= rows; j++) {
                if ((i + j) % 2 == 0)
                    System.out.print("* ");
                else
                    System.out.print("  ");
            }
            System.out.println();
        }
    }
}
