from collections import Counter


def count_unique_characters(s):
    # Count the frequency of each character in the string
    char_count = Counter(s)
    print(char_count)

    # Find characters that only occurred once
    unique_count = sum(1 for count in char_count.values() if count == 1)

    return unique_count


# Example usage
s = "examplestring"
print(f"The count of characters that occur only once: {count_unique_characters(s)}")
