def process_list(numbers):
    new_list = [num for num in numbers if num >= 0]

    new_list.append(0)

    new_list.sort()

    return new_list

#note: this is the function as asked in q2. to use it:

#original = [5, -2, 8, -1, 3]
#result = process_list(original)
#print("Original:", original)
#print("Result:", result)