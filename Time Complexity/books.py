def is_possible(books, students, max_pages):
    student_count = 1
    current_pages = 0

    for pages in books:
        if current_pages + pages > max_pages:
            student_count += 1
            current_pages = pages
            if student_count > students:
                return False
        else:
            current_pages += pages
    return True

def find_minimum_max_pages(books, students):
    if students > len(books):
        return -1  # Not enough books to assign at least one to each student

    low = max(books)
    high = sum(books)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if is_possible(books, students, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

# Input
M = int(input())
books = list(map(int, input().split()))
N = int(input())

# Output
print(find_minimum_max_pages(books, N))
