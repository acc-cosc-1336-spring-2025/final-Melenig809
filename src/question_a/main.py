from question_a import stock_purchase_history

def main():
    while True:
        print("\nStock Purchase Menu")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Please enter your choice (1 or 2): ")

        if choice == "1":
            stock_purchase_history()

        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()