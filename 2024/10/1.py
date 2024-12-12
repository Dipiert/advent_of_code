input = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
"""

"""
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
"""

# def next_step(i, j, input, step="0"):
#     if i == len(input)-2:
#         return
#     if j == len(input[i]) + 1:
#         j = 0
#         i += 1
        
#     for off in range(2):
#         if input[i+off][j] == step:
#             print(f"Found step: {step} at {(i, j)}")
#             next = str(int(step)+1)
#             if next == '9':
#                 return (i, j, '9')
#             else:
#                 return next_step(i, j+1, input, off, step)

def trailheads(i, input, step="0"):
    i = 0
    j = 0    
    next_step(i, j, input, step)


    #if step in prev_row:
    #    prev_row.index(step), str(int(step+1))
        
    # if step in row:
    #     if row.index(step) in (i+1, i-1):
    #         trailheads(row, input, "1")
    #         print(row.index(step))
    # else:
    #     pass

def find_close_steps(input, i, j, step):
    close_steps = []
    if lines[i-1][j] == step: #or lines[i][j-1] or lines[i+1][j] or input[i][j+1] == step
        close_steps.append(i-1, j)
    if lines[i][j-1] == step:
        close_steps.append(i, j-1)
    if lines[i+1][j] == step:
        close_steps.append(i+1, j)
    if input[i][j+1] == step:
        close_steps.append(i, j+1)
    return close_steps
        
        
lines = input.split("\n")[:-1]
i = 0
j = 0
step = "0"
last_found = None
for i in range(1, len(lines)-1):
    for j in range(1, len(lines[0])-1):
        
                                       
        # if lines[i][j] == step:
        #     if not last_found:
        #         last_found = (i, j)
        #     if abs(i - last_found[0]) <= 1 and abs(j - last_found[1]) <= 1:
        #         last_found = (i, j)
        #         print(f"Found step {step} at {last_found}")
        #         step = str(int(step)+1)
        
#    if trailheads(i, lines):
    #if "0" in l:
    #    print(l.index("0"))
    #else:
    #    pass