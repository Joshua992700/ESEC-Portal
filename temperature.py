def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n  # Initialize the answer array
    stack = []  # Stack to keep track of indices

    for i in range(n):
        # While there are indices in the stack and the current temperature is greater
        # than the temperature at the index stored at the top of the stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()  # Get the index of the previous temperature
            answer[idx] = i - idx  # Calculate the number of days to wait
        stack.append(i)  # Push the current index onto the stack

    return answer

# Example usage
if __name__ == "__main__":
    n = int(input())
    temperatures1 = [int(input()) for i in range(n)]
    result1 = dailyTemperatures(temperatures1)
    print(','.join(map(str,result1)))
