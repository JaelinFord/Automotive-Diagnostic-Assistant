from diagnostics import diagnostics

def run_diagnostic(start):
    current = start

    while True:
        node = diagnostics[current]

        # If result exists → stop
        if "result" in node:
            print("\n=== DIAGNOSIS RESULT ===")
            print(node["result"])
            break

        # Ask question
        answer = input(f"{node['question']} (y/n): ").lower()

        if answer == "y":
            current = node["yes"]
        elif answer == "n":
            current = node["no"]
        else:
            print("Please answer with 'y' or 'n'.")

def main():
    print("Automotive Diagnostic Assistant\n")
    print("Select issue:")
    print("1. Car won't start")

    choice = input("Enter choice: ")

    if choice == "1":
        run_diagnostic("no_start")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
