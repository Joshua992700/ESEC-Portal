import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int D = scanner.nextInt();

        int L = findLargestNumber(N, D);
        System.out.println(L);
    }

    public static int findLargestNumber(int N, int D) {
        for (int i = N - 1; i >= 0; i--) {
            if (!containsDigit(i, D)) {
                return i;
            }
        }
        return -1; // Return -1 if no such number is found
    }

    public static boolean containsDigit(int num, int digit) {
        while (num > 0) {
            if (num % 10 == digit) {
                return true;
            }
            num /= 10;
        }
        return false;
    }
}

/* 

*/
