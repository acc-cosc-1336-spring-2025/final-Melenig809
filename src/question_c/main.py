from question_c import get_most_likely_ancestor_consensus

def main():
    while True:
        dna_string1 = input("Please enter a DNA string (between 9 and 16 characters): ")
        
        if len(dna_string1) < 9 or len(dna_string1) > 16:
            print("Invalid input! DNA string must be between 9 and 16 characters long.")
            continue
        
        dna_string2 = input("Please enter a DNA substring (exactly 4 characters): ")
        
        if len(dna_string2) != 4:
            print("Invalid input! DNA substring must be exactly 4 characters long.")
            continue
        
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        
        print(f"Positions of the substring '{dna_string2}' in '{dna_string1}':")
        print(*result)
        
        exit_choice = input("\nDo you want to try again? (y/n): ").strip().lower()
        if exit_choice != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
