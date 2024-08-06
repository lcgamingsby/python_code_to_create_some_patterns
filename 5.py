class SquareStarPattern:
    def __init__(self, n):
        self.n = n

    def generate_pattern(self):
        pattern = ""
        for i in range(self.n):
            if i == 0 or i == self.n - 1:
                pattern += "*" * self.n + "\n"
            else:
                pattern += "*" + " " * (self.n - 2) + "*\n"
        return pattern


while True:
    try:
        n = int(input("Enter the value of n: "))
        if n % 1 == 0 and 1 <= n <= 60:
            break
        else:
            print("Invalid input.")
    except ValueError:
        print("Invalid input.")

pattern = SquareStarPattern(n).generate_pattern()

with open("output.txt", "a") as f:
    f.write(pattern)
    print("Success! Check output.txt for the results.")