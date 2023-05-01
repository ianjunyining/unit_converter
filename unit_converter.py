import streamlit as st

scr = "https://uploads.scratch.mit.edu/get_image/user/111367303_192x192.png"

def convert_length(from_select, to_select, input):
    length_dict = {
        "Meter" : 1,
        "Centimeter" : 0.01,
        "Feet" : 0.3048,
        "Inches" : 0.0254,
        "Millimeter" : 0.001,
        "Micrometer" : 0.000001,
        "Mile" : 1609.344,
    }
    return convert(length_dict, from_select, to_select, input)  

def convert_weight(from_select, to_select, input):
    weight_dict = {
        "Kilogram" : 1,
        "Pound" : 0.45359237,
        "Ounce" : 0.028349523,
        "Milligram" : 1e-6,
        "Microgram" : 1e-9,
        "Gram" : 0.001,
        "Ton" : 1000,
    }
    return convert(weight_dict, from_select, to_select, input)

def convert(unit_dict, from_select, to_select, input):
    from_rate = unit_dict[from_select]
    to_rate = unit_dict[to_select]
    return from_rate * input / to_rate


Unit = st.sidebar.selectbox("Opitions: ", ("Length", "Weight", "Speed", "Credits and Notes"))
if Unit == "Length":
    st.title("Length Unit Converter $$\sqrt{2\pi}(x^2 + y^2)$$")
    c1, c2, c3 = st.columns(3)
    with c1:
        from_select = st.selectbox(label_visibility="collapsed", options=("Meter", "Centimeter", "Feet", "Inches", "Millimeter", "Micrometer", "Mile"), label="")
        from_input = st.number_input("", label_visibility="collapsed")
    with c2:
        st.markdown("<h1 style='font-size: 80px; text-align: center;'>=</h1>", unsafe_allow_html=True)
    with c3:    
        to_select = st.selectbox(" ", ("Meter", "Centimeter", "Feet", "Inches", "Millimeter", "Micrometer", "Mile"), label_visibility="collapsed")
        result = convert_length(from_select, to_select, from_input)
        input = st.number_input("  ", label_visibility="collapsed", value=result)

elif Unit == "Weight":
    c1, c2, c3 = st.columns(3)
    st.title("Weight Unit Converter $$\sqrt{2\pi}(x^2 + y^2)$$")
    with c1:
        from_input = st.number_input("Value:")
        from_select = st.selectbox(label_visibility="collapsed", options=("Kilogram", "Pound", "Ounce", "Milligram", "Microgram", "Gram", "Ton"), label="")
    with c2:
        st.markdown("<h1 style='font-size: 80px; text-align: center;'>=</h1>", unsafe_allow_html=True)
    with c3:
        to_select = st.selectbox("   ", ("Kilogram", "Pound", "Ounce", "Milligram", "Microgram", "Gram", "Ton"), label_visibility="collapsed")
        result = convert_weight(from_select, to_select, from_input)
        st.text(result)
elif Unit == "Credits and Notes":
    st.title("Unit Converter - Credits")
    st.markdown("""<h5>Thanks for Huazhong for teaching me how to use streamlit</h5>
    <h5>Thanks for Ian(Me) for creating the code</h2>
    <h5>Thanks for Hengqingchu for viewing my project</h5>
    <h2>Notes</h2>
    <p>    If you are viewing this Unit Converter I would thank you for doing that. Me as the the creator when I first saw this I had fun with it and now I am a expert at it. I learned streamlit in 1 day ( Almost all the functions the python library has ). I had lots of fun coding this thing and I will make another project in the future. When I learned streamlit it was kind of easy but now learning after 1 day it became easier than the first time I coded with it. I discovered function after function and now I almost know the whole library. I also learned that it is a data based library to make websites and that you can't make clicker games or some other games. I really like this project because converting length, speed, and weight is hard but I did it.</p>""", unsafe_allow_html=True)
    st.image(scr, width=70)