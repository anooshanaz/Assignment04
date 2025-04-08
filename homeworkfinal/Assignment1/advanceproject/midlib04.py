
import streamlit as st
import random

def main():
    st.set_page_config(page_title="Personality Finder", page_icon="🔮", layout="centered")
    st.markdown("""
        <style>
            .stButton>button {
                background-color: #6A5ACD;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 18px;
            }
            .stTextInput>div>div>input {
                font-size: 20px;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🔮 Discover Your Personality")
    st.write("Enter your name and select your zodiac sign to reveal interesting details about yourself!")
    
    name = st.text_input("Enter your name:")
    zodiac_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    sign = st.selectbox("Select your Zodiac Sign:", zodiac_signs)
    
    traits = {
        "Aries": ("Bold and ambitious", "Red", "🔥"),
        "Taurus": ("Reliable and patient", "Green", "🌿"),
        "Gemini": ("Curious and adaptable", "Yellow", "💨"),
        "Cancer": ("Sensitive and intuitive", "Silver", "🌊"),
        "Leo": ("Confident and charismatic", "Gold", "🌞"),
        "Virgo": ("Practical and analytical", "Brown", "🌾"),
        "Libra": ("Balanced and diplomatic", "Pink", "⚖️"),
        "Scorpio": ("Passionate and determined", "Black", "🦂"),
        "Sagittarius": ("Adventurous and optimistic", "Purple", "🏹"),
        "Capricorn": ("Disciplined and hardworking", "Dark Blue", "⛰️"),
        "Aquarius": ("Innovative and independent", "Blue", "🌬️"),
        "Pisces": ("Compassionate and artistic", "Sea Green", "🐟"),
    }
    
    if st.button("Reveal My Personality"):
        personality, color, emoji = traits[sign]
        st.success(f"✨ {name}, you are {personality}! Your lucky color is {color} {emoji}.")

if __name__ == "__main__":
    main()
