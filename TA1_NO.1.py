
def count_chars(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = 0
    consonant_count = 0
    space_count = 0
    other_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1

    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)
    print("Number of spaces:", space_count)
    print("Number of other characters:", other_count)

# Get input from the user
user_input = input("Enter a string: ")
count_chars(user_input)
