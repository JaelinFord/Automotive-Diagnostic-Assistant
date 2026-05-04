from diagnostics import diagnostics
from obd_codes import obd_codes

import json

def log_case(issue, result):
    case = {
        "issue": issue,
        "result": result
    }

    try:
        with open("cases.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(case)

    with open("cases.json", "w") as f:
        json.dump(data, f, indent=2)

def lookup_obd_code():
    code = input("Enter OBD-II code (e.g., P0300): ").upper()

    if code in obd_codes:
        data = obd_codes[code]

        print("\n=== OBD-II DIAGNOSTIC ===")
        print(f"Code: {code}")
        print(f"Description: {data['description']}")

        print("\nPossible Causes:")
        for cause in data["causes"]:
            print(f"- {cause}")

        print("\nRecommended Actions:")
        for action in data["actions"]:
            print(f"- {action}")
    else:
        print("\nCode not found in database.")
        print("Further diagnostics required. Escalate to Level 2 support.")

def run_diagnostic(start):
    current = start

    while True:
        node = diagnostics[current]

        # If result exists → stop
        if "result" in node:
            print("\n=== DIAGNOSIS RESULT ===")
            print(node["result"])
            log_case(start, node["result"])
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
    print("2. Check engine light")
    print("3. Enter OBD-II code")

    choice = input("Enter choice: ")

    if choice == "1":
        run_diagnostic("no_start")
    elif choice == "2":
        run_diagnostic("check_engine_light")
    elif choice == "3":
        lookup_obd_code()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
