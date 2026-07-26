import streamlit as st
from base_converter import convert_base, float_to_ieee754, format_ieee754, ieee754_to_float
from alpha import characters

st.set_page_config(page_title = "Base & IEEE-754 Converter", page_icon = "🔢", layout = 'wide')

st.title("Base & IEEE-754 Converter")
st.write("Digital System Converter and IEEE-754 Standard Analyzer")

tab1, tab2 = st.tabs(["Base Converter", "IEEE-754 (Floating Point)"])

# Decimal Numbers
with tab1:
    st.subheader("Conversion of integers between different systems")

    with st.form(key = "convert_form"):

        col1, col2 = st.columns(2)

        with col1:
            input_num = st.text_input("Input an integer:", key = "base_input")
            base_from = st.number_input("Base From:", min_value = 2, max_value = 36, value = 10)
            signed = st.checkbox("Signed: ", value = False)

        with col2:
            base_to = st.number_input("Base To:", min_value = 2, max_value = 36)
            bits = st.selectbox("Bits:", options = [8, 16, 32, 64])
            twos_complement = st.checkbox("Two's Complement", value = True)

        submitted = st.form_submit_button("Convert", type="primary")

    if submitted:
        if input_num.strip():
            try:
                res = convert_base(
                    num_str=input_num,
                    base_from=base_from,
                    base_to=base_to,
                    bits=bits,
                    twos_complement=twos_complement,
                    signed=signed
                )
                st.success(f"Result in {base_to}-th system: {res}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a number")

    st.markdown("---")
    st.subheader("All major systems at the same time")
    if input_num.strip() and '.' not in input_num:
        try:
            col_b, col_q, col_o, col_d, col_h = st.columns(5)
            b_val = convert_base(input_num, base_from, 2, bits=bits, signed=signed)
            q_val = convert_base(input_num, base_from, 4, bits=bits, signed=signed)
            o_val = convert_base(input_num, base_from, 8, bits=bits, signed=signed)
            d_val = convert_base(input_num, base_from, 10, bits=bits, signed=signed)
            h_val = convert_base(input_num, base_from, 16, bits=bits, signed=signed)

            with col_b:
                st.caption("Binary (2)")
                st.code(b_val)

            with col_q:
                st.caption("Quaternary (4)")
                st.code(q_val)

            with col_o:
                st.caption("Octal (8)")
                st.code(o_val)        

            with col_d:
                st.caption("Decimal (10)")
                st.code(d_val)

            with col_h:
                st.caption("Hexadecimal (16)")
                st.code(h_val, language = "text")

        except Exception as e:
            st.info("Enter a valid number to see it on all systems.")

    # Characters Mapping

    with st.expander("Show Base 36 Character Mapping (A=10, B=11 ... Z=35)"):
        items = list(characters.items())
        cols_per_row = 6
        n = len(items)
        for i in range(0, n, cols_per_row):
            row = items[i : i + cols_per_row]
            cols = st.columns(cols_per_row)

            for j, (k,v) in enumerate(row):
                cols[j].metric(label = k, value = v)

# IEEE-754 Floating Point
with tab2:
    st.subheader("Conversion of float numbers to the IEEE-754 binary standard")
    float_input = st.number_input("Input floating number (e.g. -12.375)")

    if float_input:
        try:
            b32 = float_to_ieee754(float_input, 32)
            b64 = float_to_ieee754(float_input, 64)

            fmt32 = format_ieee754(b32)
            fmt64 = format_ieee754(b64)

            st.markdown("### 32-bit (Single Precision)")
            sign_32, exponent_32, mantissa_32, full_number_32 = st.columns(4)

            with sign_32:
                st.caption("Sign")
                st.code(fmt32["Sign"])

            with exponent_32:
                st.caption("Exponent")
                st.code(fmt32["Exponent"][0] if isinstance(fmt32["Exponent"], tuple) else fmt32["Exponent"])

            with mantissa_32:
                st.caption("Mantissa")
                st.code(fmt32["Mantissa"])

            with full_number_32:
                st.caption("Full Number")
                st.code(fmt32["Full Number"])

            st.markdown("---")
            st.markdown("### 64-bit (Double Precision)")

            sign_64, exponent_64, mantissa_64, full_number_64 = st.columns(4)

            with sign_64:
                st.caption("Sign")
                st.code(fmt64["Sign"])

            with exponent_64:
                st.caption("Exponent")
                st.code(fmt64["Exponent"][0] if isinstance(fmt64["Exponent"], tuple) else fmt64["Exponent"])

            with mantissa_64:
                st.caption("Mantissa")
                st.code(fmt64["Mantissa"])

            with full_number_64:
                st.caption("Full Number")
                st.code(fmt64["Full Number"])

        except ValueError:
            st.error("Please enter a valid decimal float number (for example, 3.14 or -12.375).")

    st.markdown("---")

    st.subheader("IEEE-754 Binary to Float")
    st.write("You can enter either a packed array or a mantissa separated by spaces (Sign Exponent Mantissa).")
    ieee_input = st.text_input("Enter the IEEE-754 binary string (32 or 64 bit):")

    if ieee_input.strip():
        try:
            float_val, full_str = ieee754_to_float(ieee_input)
            st.success(f"The resulting decimal number (Float): `{float_val}`")
            st.info(f"Recovered and complete binary code: `{full_str}` ({len(full_str)}-bit)")
        except Exception as e:
            st.error(f"Error: {e}. Check whether the input is the correct 32- or 64-bit length.")

