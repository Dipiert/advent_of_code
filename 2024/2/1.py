from pathlib import Path

def get_file_as_str(path='input.txt'):
    p = Path(__file__).with_name(path)

    with p.open("r") as f:
        file = f.read()
        
    return file



# input = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# """
input = get_file_as_str()

# def safe_with_dumpener():
#     safe = 0
#     for l in input.splitlines():
#         numbers = []
#         for n in l.split(" "):
#             numbers.append(int(n)) 
            
#         levels_to_remove = 0  
#         i = 0
#         numbers_copy = numbers[:]
#         while i < len(numbers_copy) - 1:
#             if abs(numbers_copy[i] - numbers_copy[i+1]) < 1 or abs(numbers_copy[i] - numbers_copy[i+1]) > 3:
#                 levels_to_remove += 1                
#                 numbers_copy.pop(i+1)
#                 i = 0
#             else:
#                 i += 1
#         print()
#         print(f"levels to remove: {levels_to_remove}")
#         if all(numbers[i] < numbers[i+1] for i in range(len(numbers) - 1)) and levels_to_remove <= 1:
#             print(f"{numbers} is safe")
#             safe += 1
#         elif all(numbers[i] > numbers[i+1] for i in range(len(numbers) - 1)) and levels_to_remove <= 1:
#             print(f"{numbers} is safe")
#             safe += 1
#         else:
#             print(f"{numbers} is not safe")
            
#     print(safe)
# def _count_safe(numbers):
#     safe = 0
#     if all(abs(numbers[i] - numbers[i+1]) >= 1 and abs(numbers[i] - numbers[i+1]) <= 3 for i in range(len(numbers) - 1)):
#         if all(numbers[i] < numbers[i+1] for i in range(len(numbers) - 1)):
#             safe += 1
#         elif all(numbers[i] > numbers[i+1] for i in range(len(numbers) - 1)):
#             safe += 1
#     return safe 

# 651 is too high, 562 is too low

def _problem_dampener(numbers):
    if _is_safe(numbers):
        return True

    for i in range(len(numbers)):
        modified_levels = numbers[:i] + numbers[i+1:]
        if _is_safe(modified_levels):
            return True
        
    return False  

def problem_dampener():
    safe = 0
    for l in input.splitlines():
        numbers = []
        for n in l.split(" "):
            numbers.append(int(n))
        if _problem_dampener(numbers):
            safe += 1
    print(safe)
          
    
def _is_safe(numbers):
    safe = 0
    if all(abs(numbers[i] - numbers[i+1]) >= 1 and abs(numbers[i] - numbers[i+1]) <= 3 for i in range(len(numbers) - 1)):
        if all(numbers[i] < numbers[i+1] for i in range(len(numbers) - 1)):
            return True
        elif all(numbers[i] > numbers[i+1] for i in range(len(numbers) - 1)):
            return True
    return False # 651 is too high
    
def count_safe():
    safe = 0
    for l in input.splitlines():
        numbers = []
        for n in l.split(" "):
            numbers.append(int(n))
        print(numbers)
        if _is_safe(numbers):
            safe += 1      
    #safe_count = _count_safe(numbers)
    print(safe)
    
if __name__ == '__main__':
    problem_dampener()
    #count_safe()