class InvertedRightTriangle:
    def __init__(self, n):
        self.n = n

    def display_pattern(self):
        with open('output.txt', 'a') as f:
            for i in range(self.n, 0, -1):
                for j in range(i):
                    f.write('*')
                f.write('\n')

if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    pattern = InvertedRightTriangle(n)
    pattern.display_pattern()
    print("Success! Check output.txt for the results.")