class FibonacciTriangle:
    def __init__(self, n):
        self.n = n

    def display(self):
        fib = [0, 1]
        for i in range(2, self.n):
            fib.append(fib[i - 1] + fib[i - 2])

        # Display the Fibonacci Right Triangle pattern
        with open("output.txt", "a") as f:
            for i in range(self.n):
                for j in range(i + 1):
                    f.write(str(fib[j]) + " ")
                f.write("\n")

while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

fib_tri = FibonacciTriangle(n)
fib_tri.display()
print("Success! Check output.txt for the results.")