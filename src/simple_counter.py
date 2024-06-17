
# # # closure example

def counter():
    count = 0
    def increment_count():
        nonlocal count
        count += 1
        return count
    return increment_count

do_it = counter()
for i in range(32):
    print(f'>>> current count {do_it()}')