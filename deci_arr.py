idx = set()
def find_unique_sums(numbers:list[int])->list[int]:
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
                idx.add(numbers[i]+numbers[j])
    return list(idx)
list(idx).sort()
print(find_unique_sums([1,2,3,4]))