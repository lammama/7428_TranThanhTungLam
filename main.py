import streamlit as st
import random

# Khởi tạo trạng thái mặc định
if 'player_positions' not in st.session_state:
    st.session_state.player_positions = {'Xanh': 0, 'Đỏ': 0}
if 'turn' not in st.session_state:
    st.session_state.turn = 'Xanh'
if 'winner' not in st.session_state:
    st.session_state.winner = None

# Tiêu đề
st.title("🎲 Cờ Cá Ngựa Đơn Giản")
st.markdown("Phiên bản 2 người chơi - Mỗi người có 1 quân cờ")

# Hiển thị vị trí hiện tại
st.subheader("📍 Vị trí hiện tại:")
st.text(f"🟢 Xanh: {st.session_state.player_positions['Xanh']} / 30")
st.text(f"🔴 Đỏ: {st.session_state.player_positions['Đỏ']} / 30")

# Hiển thị người chơi hiện tại
if st.session_state.winner:
    st.success(f"🎉 Người chơi {st.session_state.winner} đã chiến thắng!")
else:
    st.info(f"⬇️ Tới lượt: {st.session_state.turn}")

    if st.button("🎲 Gieo xúc xắc"):
        dice = random.randint(1, 6)
        st.write(f"🎲 Kết quả: {dice}")

        current = st.session_state.turn
        st.session_state.player_positions[current] += dice

        if st.session_state.player_positions[current] >= 30:
            st.session_state.winner = current
        else:
            # Đổi lượt
            st.session_state.turn = 'Đỏ' if current == 'Xanh' else 'Xanh'

# Nút chơi lại
if st.button("🔄 Chơi lại"):
    st.session_state.player_positions = {'Xanh': 0, 'Đỏ': 0}
    st.session_state.turn = 'Xanh'
    st.session_state.winner = None
streamlit run ludo_streamlit.py
