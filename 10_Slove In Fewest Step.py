def separate_and_sort(s):
    # Step 1: Extract and sort all alphabetic characters
    letters = sorted([ch for ch in s if ch.isalpha()])

    # Step 2: Extract and sort all digits
    digits = sorted([ch for ch in s if ch.isdigit()])

    # Step 3: Concatenate sorted letters and digits
    return ''.join(letters + digits)

# Example usage
input_str = "B4A1D3"
output = separate_and_sort(input_str)
print(output)  # Output: ABD134
