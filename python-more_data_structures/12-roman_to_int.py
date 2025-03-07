def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    # Dictionary of Roman numerals and their integer values
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    # Initialize result to 0
    total = 0
    length = len(roman_string)

    for i in range(length):
        # Get the integer value of the current Roman numeral
        current_value = roman_numerals.get(roman_string[i], 0)

        # Check if we are not at the last character and if the next numeral is larger
        if i + 1 < length:
            next_value = roman_numerals.get(roman_string[i + 1], 0)
            # If the current value is smaller than the next value, subtract it
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        else:
            # If it's the last character, just add its value
            total += current_value

   return total
