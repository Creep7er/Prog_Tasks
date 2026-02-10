lst = [1, 2, 3]
def all_subsets(lst):
    result = [[]]
    
    for kek in lst:
        new_subsets = []
        for subset in result:
            new_subset = subset + [kek]
            new_subsets.append(new_subset)
        
        result.extend(new_subsets)
    return result

all_subsets_iter = all_subsets(lst)

print(f"\nИсходный список: {lst}")
print(f"Все подмножества (количество: {len(all_subsets_iter)}):")
print(all_subsets_iter)