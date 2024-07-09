import java.util.Scanner;

public class MiddlePattern {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word = scanner.nextLine();
        
        int length = word.length();
        if (length % 2 == 0) {
            System.out.println("Please enter a word with odd length.");
            return;
        }

        int middleIndex = length / 2;
        StringBuilder output = new StringBuilder();

        for (int i = middleIndex; i < length; i++) {
            output.append(word.charAt(i));
            System.out.println(output.toString());
        }

        for (int i = 0; i < middleIndex; i++) {
            output.append(word.charAt(i));
            System.out.println(output.toString());
        }

        scanner.close();
    }
}
