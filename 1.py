class Fibonacci:
    def __init__(self, n):
        self.n = n

    def generate_sequence(self):
        a, b = 0, 1
        fib_sequence = []

        for i in range(self.n):
            fib_sequence.append(b)
            a, b = b, a + b

        return fib_sequence

    def print_sequence(self):
        fib_sequence = self.generate_sequence()
        output = ""

        for num in fib_sequence:
            output += str(num) + " "

        with open("output.txt", "a") as f:
            f.write(output + "\n\n")

        print("Fibonacci sequence of length", self.n, "has been printed to output.txt")


if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    fib = Fibonacci(n)
    fib.print_sequence()
    print("Success! Check output.txt for the results.")