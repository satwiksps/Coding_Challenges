public class factorial_tail_recursion {
    static int factorial(int n, int a) {
        if (n == 0)
            return a;
        return factorial(n - 1, n * a);
    }

    public static void main(String[] args) {
        System.out.println(factorial(5, 1));
    }
}
