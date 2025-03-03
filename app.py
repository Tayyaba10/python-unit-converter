import streamlit as st 

st.title("🔄 Unit Converter")
st.write("Welcome to the Unit Converter!")
st.write("This application allows you to convert between different units of measurement.")

st.sidebar.header("Unit Categories")
unit_categories = {
    '📏 Length': ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches']
}
unit_categories['⚖️ Weight'] = ['grams', 'kilograms', 'milligrams', 'pounds', 'ounces']
unit_categories['🌡️ Temperature'] = ['celsius', 'fahrenheit', 'kelvin']
unit_categories['⏲️ Time'] = ['seconds', 'minutes', 'hours', 'days']

selected_category = st.sidebar.selectbox("Select Unit Category:", list(unit_categories.keys()))
units = unit_categories[selected_category]

def convert_units(value, from_unit, to_unit,category):
    if category == '📏 Length':
        conversion_factors = {
            'meters': 1.0,
            'kilometers': 0.001,
            'centimeters': 100.0,
            'millimeters': 1000.0,
            'miles': 0.000621371,
            'yards': 1.09361,
            'feet': 3.28084,
            'inches': 39.3701
        }
        return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

    elif category == '⚖️ Weight':
        conversion_factors = {
            'grams': 1.0,
            'kilograms': 0.001,
            'milligrams': 1000.0,
            'pounds': 0.00220462,
            'ounces': 0.035274
        }
        return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

    elif category == '🌡️ Temperature':
        if from_unit == 'celsius' and to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif from_unit == 'fahrenheit' and to_unit == 'celsius':
            return (value - 32) * 5/9
        elif from_unit == 'celsius' and to_unit == 'kelvin':
            return value + 273.15
        elif from_unit == 'kelvin' and to_unit == 'celsius':
            return value - 273.15
        elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return None
    elif category == '⏲️ Time':
        conversion_factors = {
            'seconds': 1.0,
            'minutes': 1/60,
            'hours': 1/3600,
            'days': 1/86400
        }
    else:
        return None

st.header(f"Convert {selected_category}")
value = st.number_input("Enter the value:", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From Unit:",units)
to_unit = st.selectbox("To Unit:", units)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, selected_category)
    if result is not None:
        st.success(f"{value} {from_unit} is equal to {result} {to_unit}")
    else:
        st.error("Invalid unit conversion")
