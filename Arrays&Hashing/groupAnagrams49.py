# Again something that could be done in time O(n²) and space O(n)
# Here its solved in time O(n) and space O(n)

# We sort the word and check if its in the result dict.
# If its in  the dict we append the word to the array.
# If its not in it we append it to the dict with the sorted word as the key and the unsorted word as a value inside an array.

def groupAnagrams(strs):
    result = {}
    for word in strs:
        sortedWord = ''.join(sorted(word))
        if sortedWord in result:
            result[sortedWord].append(word)
        else:
            result[sortedWord] = [word]
    return  list(result.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))