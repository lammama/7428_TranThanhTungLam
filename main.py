import streamlit as st

st.set_page_config(page_title="🎮 Mario Game", layout="wide")

st.title("🎮 Chơi Mario ngay trên trình duyệt!")

st.markdown("Mario HTML5 mini game được nhúng dưới đây:")

# Nhúng game Mario HTML5 từ Internet (hoặc tự host)
mario_game_url = "https://supermarioemulator.com/mario.php"

st.components.v1.iframe(src=mario_game_url, width=800, height=600, scrolling=False)
