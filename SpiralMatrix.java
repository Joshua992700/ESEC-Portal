import java.util.Scanner;

public class SpiralMatrix {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read matrix dimensions
        int rows = scanner.nextInt();
        int cols = scanner.nextInt();

        // Initialize the matrix
        int[][] matrix = new int[rows][cols];

        // Fill the matrix
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }

        // Print the matrix in spiral form
        printSpiral(matrix, rows, cols);
    }

    private static void printSpiral(int[][] matrix, int rows, int cols) {
        int top = 0, bottom = rows - 1;
        int left = 0, right = cols - 1;

        while (top <= bottom && left <= right) {
            // Traverse down the leftmost column
            for (int i = top; i <= bottom; i++) {
                System.out.print(matrix[i][left] + " ");
            }
            left++;

            // Traverse across the bottom row
            for (int i = left; i <= right; i++) {
                System.out.print(matrix[bottom][i] + " ");
            }
            bottom--;

            // Traverse up the rightmost column, if there's anything left
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    System.out.print(matrix[i][right] + " ");
                }
                right--;
            }

            // Traverse across the top row, if there's anything left
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    System.out.print(matrix[top][i] + " ");
                }
                top++;
            }
        }
    }
}
