def create_multiplication_table():
    table = []

    for i in range(1, 11): 
        row = []  
        for j in range(1, 11):  
            row.append(i * j)  
        table.append(row)  
    
    return table

def display_multiplication_table(table):
    for row in table:
        print(" ".join(str(value) for value in row))

if __name__ == "__main__":
    multiplication_table = create_multiplication_table()
    
    display_multiplication_table(multiplication_table)
