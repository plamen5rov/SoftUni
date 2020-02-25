target_book = input()

library_books = int(input())

counter = 0

book_found = False

while counter < library_books:
    current_book = input()
    counter += 1
    if current_book == target_book:
        book_found = True
        print(f'You checked {counter - 1} books and found it.')
        break


if not book_found:
    print('The book you search is not here!')
    print(f'You checked {counter} books.')
