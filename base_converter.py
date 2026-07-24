"""
Base Converter (bin, oct, dec and hex).\n
This also supports IEEE-754 floating point standard 32 or 64 bits.
"""
import string
import struct

def base_to_int(num_str: str, base_from: int, signed:bool = False) -> int:
    """
    Converts signed or unsigned integer from given base to decimal integer.\n
    E.g.
        base_to_int("13", 8, signed=False) --> 11
        base_to_int("D8", 16, signed=True) --> -40
    """
    num_str = num_str.upper().strip()
    val = int(num_str, base_from)

    if signed and len(num_str) > 0:
        first_digit_char = num_str[0]
        digits = string.digits + string.ascii_uppercase
        first_digit_val = digits.index(first_digit_char)

        limit = (base_from + 1) // 2

        if first_digit_val >= limit:
            num_digits = len(num_str)
            max_value = base_from ** num_digits
            val = val - max_value

    return val

def int_to_base(num: int, base_to: int, bits: int = 32, twos_complement: bool = True) -> str:
    """
    Converts decimal integer to given base.\n
    E.g.
        int_to_base(-12, 2, bits=8, twos_complement=False) --> 11110100
        int_to_base(18, 8) --> 22
    """
    if num == 0:
        return "0"

    digits = string.digits + string.ascii_uppercase
    if base_to > len(digits):
        raise ValueError("Base too large (max 36)")

    # Handle negative numbers with two's complement
    if num < 0 and twos_complement:
        num = (1 << bits) + num   # 2^bits + num
        if num < 0:
            raise ValueError("Number too small for given bit width")

    result = []
    while num > 0:
        result.append(digits[num % base_to])
        num //= base_to

    return "".join(reversed(result)) if result else "0"

def convert_base(num_str: str, base_from: int, base_to: int, bits: int = 32, twos_complement: bool = True, signed: bool = False) -> str:
    """
    Converts number from one base to another.\n
    E.g.
        convert_base("23", 10, 16) --> 17
        convert_base("D4", 16, 2, bits=8 ,signed=True) --> 11010100
        convert_base("342", 5, 9, signed=False) --> 117
    """
    try:
        decimal_val = base_to_int(num_str, base_from, signed=signed)
        if decimal_val < 0 and base_to == 10:
            return str(decimal_val)
        
        return int_to_base(decimal_val, base_to, bits=bits, twos_complement=twos_complement)
    except ValueError:
        if base_from == 10:
            return str(float(num_str))
        raise ValueError("Float conversion is currently only supported from base 10")

def get_bases(num_str:str, base:int, signed:bool = False) -> dict[str]:
    """
    Shows Bin, Quaternary, Octal, Decimal, Hexadecimal bases or IEEE-754 32/64 bit details if the given number is float.
    """
    is_float = '.' in num_str
    result = {
        "Number" : num_str,
        "Base" : base,
        "Signed" : signed
    }

    if not is_float:
        result.update({
            "Bin" : convert_base(num_str, base, 2, signed=signed),
            "Quaternary (4-base)" : convert_base(num_str, base, 4, signed=signed),
            "Oct" : convert_base(num_str, base, 8, signed=signed),
            "Dec" : convert_base(num_str, base, 10, signed=signed),
            "Hex" : convert_base(num_str, base, 16, signed=signed)
        })
    else:
        if base == 10:
            val_float = float(num_str)
            b32 = float_to_ieee754(val_float, 32)
            b64 = float_to_ieee754(val_float, 64)

            result.update({
                "IEEE-754 32-bit": format_ieee754(b32, 32),
                "IEEE-754 64-bit": format_ieee754(b64, 64)
            })
        else:
            result["Error"] = "Float analysis is only supported from base 10 in this demo."
    return result

# --- IEEE-754 Functions ---

def float_to_ieee754(num_float:float, bits:int = 32) -> str:
    """ Converts float number to binary string (IEEE-754 standard) 32 or 64 bits """
    if bits == 32:
        # 'f' -> float (32-bit single precision)
        # 'I' -> unsigned int (32-bit)
        packed = struct.pack(">f", num_float)
        integ = struct.unpack(">I", packed)[0]
        return f"{integ:032b}"
    elif bits == 64:
        # 'd' -> double (64-bit double precision)
        # 'Q' -> unsigned long long (64-bit)
        packed = struct.pack(">d", num_float)
        integ = struct.unpack(">Q", packed)[0]
        return f"{integ:064b}"
    else:
        raise ValueError("Bits must be either 32 or 64")

def ieee754_to_float(binary_str:str) -> tuple[float, str]: # (float_value, full_str)
    """ IEEE-754 binary string to Float """
    parts = binary_str.strip().split()
    if len(parts) < 2:
        clean_str = binary_str.replace(" ", "")
        bits = len(clean_str)
        if bits != 32 or bits != 64:
            raise ValueError("String without spaces must be exactly 32 or 64 bit.")
        full_str = clean_str
    else:
        sign = parts[0]
        exponent = parts[1]
        mantissa = parts[2] if len(parts) > 2 else ""

        if len(exponent) == 8:
            mantissa_len = 23
        elif len(exponent) == 11:
            mantissa_len = 52
        else:
            raise ValueError("Exponent must be 8 or 11 bits.")

        mantissa = mantissa.ljust(mantissa_len, '0')
        full_str = sign + exponent + mantissa

    bits = len(full_str)
    if bits == 32:
        integ = int(full_str, 2)
        packed = struct.pack(">I", integ)
        return (struct.unpack(">f", packed)[0], full_str)
    elif bits == 64:
        integ = int(full_str, 2)
        packed = struct.pack(">Q", integ)
        return (struct.unpack(">d", packed)[0], full_str)
    raise ValueError("Unknown error related to the bit length.")

def format_ieee754(binary_str:str) -> dict[str]:
    """Splits IEEE-754 to Sign, Exponent and Mantissa for better vision."""
    binary_str = binary_str.replace(" ", "")
    bits = len(binary_str)

    if bits == 32:
        return {
            "Type" : "32-bit (Single Precision)",
            "Full Number" : binary_str,
            "Sign" : binary_str[0],
            "Exponent" : (binary_str[1:9], int(binary_str[1:9], 2)),
            "Mantissa" : binary_str[9:]
        }
    elif bits == 64:
        return {
            "Type" : "64-bit (Double Precision)",
            "Full Number" : binary_str,
            "Sign" : binary_str[0],
            "Exponent" : (binary_str[1:12], int(binary_str[1:12], 2)),
            "Mantissa" : binary_str[12:]
        }
    return {
        "Error" : "Invalid bit length"
    }

