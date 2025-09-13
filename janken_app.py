import streamlit as st
import random

st.title("じゃんけんゲーム")

# ユーザーの選択肢
choices = ["グー", "チョキ", "パー"]
user_choice = st.radio("あなたの手を選んでください", choices)

# 勝負開始ボタン
if st.button("勝負！"):
    computer_choice = random.choice(choices)
    st.write(f"コンピュータの手: {computer_choice}")
    st.write(f"あなたの手: {user_choice}")

    if user_choice == computer_choice:
        st.success("あいこです！")
    elif (user_choice == "グー" and computer_choice == "チョキ") or \
         (user_choice == "チョキ" and computer_choice == "パー") or \
         (user_choice == "パー" and computer_choice == "グー"):
        st.success("あなたの勝ち！🎉")
    else:
        st.error("あなたの負け…😢")
