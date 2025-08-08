# import streamlit as st
# import base64

# # Hide default Streamlit UI
# st.markdown("""
#     <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}
        
#     </style>
# """, unsafe_allow_html=True)

# # Load background image
# def set_background(image_file):
#     with open(image_file, "rb") as image:
#         encoded = base64.b64encode(image.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/jpg;base64,{encoded}");
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # Set background
# set_background("image\WhatsApp Image 2025-08-02 at 8.31.52 PM.jpeg")

# # Center the button
# st.markdown("<br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     if st.button("💓 Heart Failure Check-Up", use_container_width=True):
#         st.switch_page("pages/main.py")




# import streamlit as st
# import base64

# # 🔒 Hide the multi-page sidebar selector
# st.markdown("""
#     <style>
#         [data-testid="stSidebarNav"] {
#             display: none;
#         }
#         #MainMenu, header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # 🔄 Set background image
# def set_background(image_path):
#     with open(image_path, "rb") as img_file:
#         encoded_string = base64.b64encode(img_file.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/jpeg;base64,{encoded_string}");
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # 📷 Set the background
# set_background("image/WhatsApp Image 2025-08-02 at 8.31.52 PM.jpeg")  # use forward slashes or raw string

# # 🧭 Centered button
# st.markdown("<br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     if st.button("💓 Heart Failure Check-Up", use_container_width=True):
#         st.switch_page("pages/main.py")  # Must be inside pages/





import streamlit as st
import base64

# Hide sidebar and extras
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
        #MainMenu, header, footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# Background image function
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image
set_background("image/WhatsApp Image 2025-08-02 at 8.31.52 PM.jpeg")

# Centered transparent colorful button with Streamlit
st.markdown("<br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Custom CSS
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background: rgba(255, 255, 255, 0.2);
            color: white;
            border: 2px solid white;
            border-radius: 20px;
            padding: 1rem 2rem;
            font-size: 20px;
            font-weight: bold;
        }
        div.stButton > button:first-child:hover {
            background-color: rgba(255,255,255,0.4);
            color: black;
            border: 2px solid black;
        }
        </style>
    """, unsafe_allow_html=True)

    # Correct use of switch_page with page name
    if st.button("💓 Heart Failure Check-Up", use_container_width=True):
        st.switch_page("pages/main.py")  # Use the correct page name, not path
