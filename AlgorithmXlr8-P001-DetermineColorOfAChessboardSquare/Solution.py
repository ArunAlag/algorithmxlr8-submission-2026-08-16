def main():
    coordinates = input().strip()

    # Write your solution here.
    # Print "White" or "Black".
    #cols = ["a","b","c","d","e","f","g","h"]
    #is_col_even = True
    #is_row_even = True
    
    #for i in range(len(cols)):
    #    if cols[i] == coordinates[0]:
   #         if i % 2 != 0:
    #            is_col_even = False

    #if (int(coordinates[1]) - 1) % 2 != 0:
    #    is_row_even = False

    
    #if (is_col_even and is_row_even) or ( not is_col_even and not is_row_even) : 
    #    print('Black')
    #else :
    #    print('White')

    # Second Approach (Optimized)
    cols = ["a","b","c","d","e","f","g","h"]
    col_index = cols.index(coordinates[0])
    row_index = int(coordinates[1]) -1 

    if(col_index + row_index) % 2 == 0:
        print("Black")
    else:
        print("White")

if __name__ == "__main__":
    main()
