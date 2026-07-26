characters = {
    "A":10, "B":11, "C":12, "D":13, "E":14, "F":15,
    "G":16, "H":17, "I":18, "J":19, "K":20, "L":21,
    "M":22, "N":23, "O":24, "P":25, "Q":26, "R":27,
    "S":28, "T":29, "U":30, "V":31, "W":32, "X":33,
    "Y":34, "Z":35
}

def show_characters_mapping() -> None:
    """
    Show Base 36 Character Mapping (A=10, B=11 ... Z=35)
    """
    items = list(characters.items())

    cols = 6
    max_len = max(len(f"{k}:{v}") for k,v in items)

    for i in range(0,len(items),cols):
        row = items[i:i+cols]
        row_str = " | ".join(f"{k}:{v}".ljust(max_len) for k,v in row)
        print(row_str)
        print("-" * len(row_str))
