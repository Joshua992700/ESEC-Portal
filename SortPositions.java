import java.util.*;

public class SortPositions {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Reading input
        int n = scanner.nextInt(); // number of elements
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt(); // reading the elements
        }

        // Sorting elements in odd positions in descending order
        for (int i = 0; i < n; i += 2) {
            for (int j = i + 2; j < n; j += 2) {
                if (arr[i] < arr[j]) {
                    // Swap elements
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        // Sorting elements in even positions in ascending order
        for (int i = 1; i < n; i += 2) {
            for (int j = i + 2; j < n; j += 2) {
                if (arr[i] > arr[j]) {
                    // Swap elements
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        // Printing the sorted array
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        scanner.close();
    }
}
