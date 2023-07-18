# Luwanga Number Converter
Luwanga is a dialect of the larger conglomeration of dialects, which constitute the Luhya language, and which is spoken by inhabitants of Western Kenya. The Luwanga Number Converter is a Python application that allows you to convert numerical numbers to their Luwanga word representations and vice versa. The application is designed as a learning exercise for understanding Regular Expressions in Theory of Computing, a Computer Science Undergraduate Course.

# How it Works
The application currently supports numerical numbers between 0 and 100, inclusive. It utilizes a set of predefined mappings in the luwanga_numbers dictionary to convert numerical numbers to their corresponding Luwanga words. For example, it can accurately convert numbers like 5, 20, 45, 60, and 100 to their respective Luwanga word representations.

For numbers less than 100, the application breaks them down into tens and ones, and then combines the Luwanga word representations for these parts. For example, the number 45 is split into 40 (makhumi kane) and 5 (tsirano), and the application combines them as "makhumi kane na tsirano."

The luwanga_to_number function allows you to convert Luwanga words back to numerical numbers. It can handle certain Luwanga words like "kumi" (10), "makhumi kabiri" (20), etc., and it can recognize the word "na" (and) as a separator between numbers in Luwanga.

# Future Extensions
1. *Handling Larger Numbers:* To support numbers beyond 100, you can expand the luwanga_numbers dictionary to include mappings for thousands, millions, and so on.

2. *Decimal and Fraction Support:* Modify the functions to handle decimal numbers and fractions in both numerical and Luwanga word representations.

3. *Enhance Luwanga Parsing:* Improve the Luwanga-to-number conversion logic to handle more complex structures and patterns in the Luwanga language.

4. *Error Handling:* Implement better error handling for invalid inputs or cases where the input does not match any known patterns.


# Getting Started
1. Install the required dependencies by running: pip install streamlit.

2. Run the application using the command: streamlit run luwanga_converter.py.

3. The application will launch in your default web browser, allowing you to interact with it.

# Contributing
We welcome contributions to improve and extend the functionality of the Luwanga Number Converter. If you have any ideas or improvements, feel free to open an issue or submit a pull request.

# Credits
The Luwanga Number Converter application was created by **Melinda Chebet & Oyori Obegi** for the Theory of Computation Class, 2023.


Test the app [here](https://luwangaconverter-5ma1ms46wds.streamlit.app/)
