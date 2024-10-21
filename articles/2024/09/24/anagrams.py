def group_anagrams(strs):
    from collections import defaultdict
    
    # Create a dictionary to store the grouped anagrams
    anagram_dict = defaultdict(list)
    
    # Iterate through each string in the list
    for s in strs:
        # Sort the string and use it as a key
        key = ''.join(sorted(s))
        # Append the original string to the list of its corresponding key
        anagram_dict[key].append(s)
    
    # Return the values of the dictionary as a list of lists
    return list(anagram_dict.values())

# Example usage
input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input_list))