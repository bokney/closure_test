
# # # # closure example # # # #

def simple_counter():
    count = 0
    def increment_count():
        nonlocal count
        count += 1
        return count
    return increment_count

def step_counter():
    step_count = 0
    def increment_step(step):
        nonlocal step_count
        step_count += step
        return step_count
    return increment_step

# # # # # # # # # # # # # # # #

do_it_simply = simple_counter()
for i in range(8):
    print(f'>>> current count {do_it_simply()}')

do_it_in_steps = step_counter()
step_size = 32
for i in range(8):
    print(f'>>> current count {do_it_in_steps(step_size - 2 * i)}')
