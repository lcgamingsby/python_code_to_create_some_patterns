class RightTriangle:
    def __init__(self, n):
        self.n = n

    def display_triangle(self):
        with open("output.txt", "a") as f:
            f.write(f"Right triangle star pattern for n = {self.n}\n")
            for i in range(1, self.n+1):
                for j in range(1, i+1):
                    f.write("* ")
                f.write("\n")
            f.write("\n")

if __name__ == "__main__":
    while True:
        n = int(input("Enter a positive integer value of n: "))
        rt = RightTriangle(n)
        rt.display_triangle()
        print("Success! Check output.txt for the results.")