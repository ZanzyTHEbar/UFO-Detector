def Welcome(input):
    # userName = input("Enter you name: ")
    print("Welcome " + input)

def main():
    if Welcome() == "James":
        return 1
        # print("Please enter your name")
    print("Hello, this program is still in development")
    Welcome("John")
    return 0


if __name__ == "__main__":
    if main() == 0:
        print("Program finished")