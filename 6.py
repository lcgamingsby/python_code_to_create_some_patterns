class NumberPattern:
    def __init__(self):
        self.output_file = "output.txt"

    def display_pattern(self, n):
        if n % 3 != 0 or n < 3 or n > 60:
            print("Invalid input, enter a value for n between 3-60 and n is a multiple of three")
            return False

        pattern1 = "+".join([str(i) for i in range(3, n+1, 3)])
        pattern2 = " x ".join([str(i) for i in range(2, 6)]) + " = " + str(2*3*5)
        pattern3 = "+".join([str(i) for i in [5, 10, 30]])

        with open(self.output_file, "a") as file:
            file.write(f"{pattern1}={eval(pattern1)}\n")
            file.write(f"{pattern2}\n")
            file.write(f"{pattern3}={eval(pattern3)}\n")

        return True

if __name__ == "__main__":
    obj = NumberPattern()

    while True:
        n = input("Enter a value for n between 3-60 and n is a multiple of three: ")

        if n.isdigit():
            n = int(n)

            if obj.display_pattern(n):
                print("Success! Check output.txt for the results.")
                break
        else:
            print("Invalid input, enter a positive integer value for n.")
