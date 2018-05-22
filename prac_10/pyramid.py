def main():
    row_number = int(input("Please enter Rows: "))

    block_number = calc_rows(row_number)
    print(block_number)

    block_number = calc_rows_rec(row_number)
    print(block_number)


def calc_rows(row_number):
    block_number = 0
    for i in range(row_number):
        block_number += i + 1
    return block_number


def calc_rows_rec(row_number):

    return calc_rows(row_number + 1)

if __name__ == '__main__':
    main()
