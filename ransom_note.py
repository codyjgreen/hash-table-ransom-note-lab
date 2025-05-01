def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # Create a dictionary to count characters manually
    magazine_counts = {}

    for char in magazine:
        if char in magazine_counts:
            magazine_counts[char] += 1
        else:
            magazine_counts[char] = 1

    for char in ransomNote:
        if char not in magazine_counts or magazine_counts[char] == 0:
            return False
        magazine_counts[char] -= 1

    return True

