import java.util.Stack;

public class DecodeString {
    public static String decodeString(String s) {
        Stack<Pair> stack = new Stack<>();
        int currentNum = 0;
        String currentStr = "";

        for (char ch : s.toCharArray()) {
            if (Character.isDigit(ch)) {
                currentNum = currentNum * 10 + (ch - '0'); // Build the current number
            } else if (ch == '[') {
                // Push the current number and string onto the stack
                stack.push(new Pair(currentStr, currentNum));
                currentStr = ""; 
                currentNum = 0; // Reset for the new segment
            } else if (ch == ']') {
                // Pop from the stack and construct the string
                Pair last = stack.pop();
                currentStr = last.str + currentStr.repeat(last.num); // Repeat the current string
            } else {
                currentStr += ch; // Build the current string
            }
        }

        return currentStr;
    }

    static class Pair {
        String str;
        int num;

        Pair(String str, int num) {
            this.str = str;
            this.num = num;
        }
    }

    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        String s = scanner.nextLine();
        String x = decodeString(s);
        System.out.println(x);
        scanner.close();
    }
}

/* 
Input
3[a]2[bc]

Result
aaabcbc
*/
