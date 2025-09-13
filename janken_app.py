import streamlit as st
import random

st.title("闇のじゃんけんゲーム 🔥☠️🔥")

# 初期化（最初にアプリを開いたときだけ実行）
if "win_streak" not in st.session_state:
    st.session_state.win_streak = 0
if "best_streak" not in st.session_state:
    st.session_state.best_streak = 0

choices = ["グー", "チョキ", "パー"]
user_choice = st.radio("貴様の手を差し出せ。", choices)

if st.button("運命のボタン"):
    computer_choice = random.choice(choices)
    st.write(f"コンピュータの手: {computer_choice}")
    st.write(f"あなたの手: {user_choice}")

    if user_choice == computer_choice:
        st.info("あいこだ。耐えたな。")
        # 連勝記録は変化なし
    elif (user_choice == "グー" and computer_choice == "チョキ") or \
         (user_choice == "チョキ" and computer_choice == "パー") or \
         (user_choice == "パー" and computer_choice == "グー"):
        st.session_state.win_streak += 1
        # 最高連勝記録の更新チェック
        if st.session_state.win_streak > st.session_state.best_streak:
            st.session_state.best_streak = st.session_state.win_streak
        st.success(f"フンッ お前の勝ちだ。お前が耐えた命の数⇒{st.session_state.win_streak} ")
    else:
        st.error("お前の負けェェェェェ!!!「命はリセットされました」 ...GAME OVER...")
        st.session_state.win_streak = 0

# 連勝記録を常に表示
st.write(f"👉 お前が耐えた命の数: {st.session_state.win_streak}")
st.write(f"⚖️ 過去一 粘った奴 : {st.session_state.best_streak}")
