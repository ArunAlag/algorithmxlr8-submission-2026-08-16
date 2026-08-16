def main():
    num = input().strip()

    # Write your solution here.
    # Print the maximum number after changing at most one digit 6 to 9.

    num_list = list(num)
    for i in range(len(num_list)):
        if num_list[i] == '6':
            num_list[i] = '9'
            break

    print ("".join(num_list))


if __name__ == "__main__":
    main()
