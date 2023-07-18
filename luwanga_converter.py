import streamlit as st
import re

luwanga_numbers = {
    0: 'sufuri',
    1: 'ndala',
    2: 'tsibiri',
    3: 'tsitaru',
    4: 'tsine',
    5: 'tsirano',
    6: 'sita',
    7: 'saba',
    8: 'munane',
    9: 'tisa',
    10: 'kumi',
    20: 'makhumi kabiri',
    30: 'makhumi kararu',
    40: 'makhumi kane',
    50: 'makhumi karano',
    60: 'makhumi sita',
    70: 'makhumi saba ',
    80: 'makhumi munane',
    90: 'makhumi tisa',
    100: 'imia ndala'
}

def number_to_luwanga(n):
    if n in luwanga_numbers:
        return luwanga_numbers[n]

    if n < 100:
        tens, ones = divmod(n, 10)
        if ones == 0:
            return f'{luwanga_numbers[tens * 10]}'
        else:
            return f'{luwanga_numbers[tens * 10]} na {luwanga_numbers[ones]}'

def luwanga_to_number(string):
    number_mapping = {v: k for k, v in luwanga_numbers.items()}
    words = string.lower().split()  # Convert the string to lowercase before splitting
    numerical_number = 0

    if string.lower() in number_mapping:  # Check the lowercase version of the string in the dictionary
        return number_mapping[string.lower()]

    # Regular expression pattern to match numbers like 'kumi', 'ishirini', etc.
    number_pattern = r'\b(?:kumi|makhumi kabiri|makhumi kararu|makhumi kane|makhumi karano|makhumi sita|makhumi saba|makhumi munane|makhumi tisa)\b'
    # Regular expression pattern to match the separator 'na'
    separator_pattern = r'\bna\b'

    # Join the words together to form the input string
    input_string = ' '.join(words)

    # Use regular expressions to detect and extract the numerical values and separator
    matches = re.findall(number_pattern, input_string)
    separator_matches = re.findall(separator_pattern, input_string)

    # Calculate the numerical number by summing up the extracted numerical values
    numerical_number = sum(number_mapping[match] for match in matches)

    # Check if 'na' is present, and adjust the numerical number accordingly
    if len(separator_matches) == 1 and matches:
        index = input_string.index('na')
        prefix = input_string[:index].strip()
        suffix = input_string[index + 2:].strip()
        if prefix in number_mapping and suffix in number_mapping:
            numerical_number += number_mapping[suffix]

    return numerical_number

def main():
    st.title("Luwanga Number Converter")
    st.write("The Luwanga Number Converter app allows you to convert numerical numbers to Luwanga language words and vice versa. This application currently supports numerical numbers between 0 and 100, inclusive. Enter a number or a Luwanga word and select the corresponding input type.")

    input_type = st.selectbox("Input Type:", ("Number", "Luwanga Word"))
    user_input = st.text_input("Enter your Input:")

    if input_type == "Number":
        try:
            number = int(user_input)
            result = number_to_luwanga(number)
            st.write(f"Luwanga: {result}")
        except ValueError:
            st.write("Invalid input. Please enter a valid number.")
    else:
        result = luwanga_to_number(user_input)
        st.write(f"Number: {result}")

    st.write("\n")  # Add vertical space
    st.write("Created by **Melinda Chebet and Oyori Obegi** for Theory of Computation CAT 2 2023")

if __name__ == "__main__":
    main()
