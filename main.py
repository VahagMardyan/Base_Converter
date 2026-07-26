import json
from base_converter import convert_base, get_bases, ieee754_to_float, format_ieee754, float_to_ieee754
from alpha import show_characters_mapping

# --- Input / Output ---
if __name__ == "__main__":
    print("Choose the option:")
    print("1 --> Standard Conversion (Int / Float to IEEE)")
    print("2 --> From IEEE-754 to Decimal Float")
    print("alpha / a --> Show Base 36 Character Mapping (A=10, B=11 ... Z=35)")
    print("q (or any other key) --> Close the program")
    choice = input("Option: ").strip()

    if choice == "1":
        num = input("Number: ")
        from_base = int(input("From base: "))
        if '.' in num:
            if from_base == 10:
                val_float = float(num)
                b32 = float_to_ieee754(val_float, 32)
                b64 = float_to_ieee754(val_float, 64)
    
                result = {
                    "Number" : num,
                    "IEEE-754 32-bit" : format_ieee754(b32),
                    "IEEE-754 64-bit" : format_ieee754(b64),
                }
                print("\n--- IEEE-754 Analysis ---")
                print(json.dumps(result, indent=4, ensure_ascii=False))
            else:
                print("Float analysis is only supported from base 10.")
        else:
            to_base = int(input("To base: "))

            signed_input = input("Is the input number signed ? (y/n): ").lower()
            is_signed = True if signed_input == 'y' else False
            query = input("Do you want to get bin, quaternary (4-base), oct, dec and hex conversions too? (y/n): ")

            try:
                print(convert_base(num, from_base, to_base, signed=is_signed))
                if query.lower() == 'y':
                    print(json.dumps(get_bases(num, from_base, signed=is_signed), indent=4))
            except Exception as e:
                print(f"Error during conversion: {e}")

    elif choice == "2":
        ieee_str = input("Input IEEE-754 number (32 or 64 bits): ")
        try:
            decimal_float, full_padded_str = ieee754_to_float(ieee_str)
            components = format_ieee754(full_padded_str)
            
            output = {
                "Parsed Structure" : components,
                "Decimal Float Value" : decimal_float
            }
            print("\n--- IEEE-754 Decode Result ---")
            print(json.dumps(output, indent=4, ensure_ascii=False))
        except Exception as e:
            print(f"Error: {e}.")

    elif choice in ("alpha", 'a'):
        print("---------------------------------------")
        show_characters_mapping()

    else:
        print("Closing Program...")
        exit()
        