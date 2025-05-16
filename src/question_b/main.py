from question_b import get_stock_list

def main():
    while True:
        print("\nStock Purchase Menu")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Please enter your choice (1 or 2): ")

        if choice == "1":
            stock_list = get_stock_list()

            print(f"{'Company':<15} {'Symbol'}")
            print("-" * 25)  
            for stock in stock_list:
                print(f"{stock.get_company_name():<15} {stock.get_symbol()}")

        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
