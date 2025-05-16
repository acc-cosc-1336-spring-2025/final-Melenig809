from question_d import create_multiplication_table, display_multiplication_table

def main():
    while True:
        multiplication_table = create_multiplication_table()
        
        display_multiplication_table(multiplication_table)

        exit_choice = input("\nDo you want to see the table again? (y/n): ").strip().lower()
        if exit_choice != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
