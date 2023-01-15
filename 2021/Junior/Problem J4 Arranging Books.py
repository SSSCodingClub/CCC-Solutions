from queue import Queue

books = input()

L = books.count("L")
M = books.count("M")
S = books.count("S")


def is_sorted(shelf):
    j = 0
    for i in range(L):
        if shelf[j] != "L":
            return False
        j += 1
    for i in range(M):
        if shelf[j] != "M":
            return False
        j += 1
    for i in range(S):
        if shelf[j] != "S":
            return False
        j += 1
    return True


def insert(string, index, value):
    return string[:index] + value + string[index + 1:]


def swap(shelf, i, j):
    temp = shelf[i]
    shelf = insert(shelf, i, shelf[j])
    shelf = insert(shelf, j, temp)

    return shelf


q = Queue()
q.put((books, 0))
while True:
    current, swaps = q.get()

    if is_sorted(current):
        print(swaps)
        quit()

    for i in range(len(books)):
        for j in range(len(books)):
            q.put((swap(current, i, j), swaps + 1))







# class Section:
#
#     def __init__(self):
#         self.L = 0
#         self.M = 0
#         self.S = 0
#
#     def add_book(self, book):
#         if book == "L":
#             self.L += 1
#         elif book == "M":
#
#
#
# books = input()
#
# total = len(books)
# nL = books.count("L")
# nM = books.count("M")
# nS = books.count("S")
#
# large_section = books[:nL]
# medium_section = books[nL:nM + nL]
# small_section = books[nM + nL:]
#
# print(total, large_section, medium_section, small_section)