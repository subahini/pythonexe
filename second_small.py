def find_second_smallest(args):
    first= min(args)
    args.pop(args.index(first))
    second = min(args)
    return second

print(find_second_smallest([0, 3, -2, 4, 3, 2]))
print(find_second_smallest([10, 22, 10, 20, 11, 22]))