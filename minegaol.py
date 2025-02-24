import streamlit as st
from random import shuffle

"""
# GOAL MINE
That's why you should not play games of chance
"""



if "squares" not in st.session_state:
    st.session_state.squares = [True, True, True, True, False] 
    shuffle(st.session_state.squares)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "choices" not in st.session_state:
    st.session_state.choices = []  

st.write("Squares sequence:") 
st.write(st.session_state.squares)

st.write(f"Attempt {st.session_state.attempts + 1} out of 5")


chosen_square = st.number_input("Chose a square (0-4)", min_value=0, max_value=4, step=1)

if st.button("Validate my answer") and st.session_state.attempts < 5:
    st.session_state.choices.append(chosen_square)
    
    if st.session_state.squares[chosen_square]:
        st.write(f"Attempt {st.session_state.attempts + 1}: You pass to the next level!")
        st.session_state.attempts += 1
        if st.session_state.attempts < 5:
            if st.session_state.attempts == 3:
                st.session_state.squares = [True, True, True, False, False]
                shuffle(st.session_state.squares)
            else:
                st.session_state.squares = [True, True, True, True, False]
                shuffle(st.session_state.squares)
    else:
        st.write(f"Attempt {st.session_state.attempts + 1}: You have been thwarted, you lost possesion of the ball!")
        st.write("Press on new game if you want to start a new match")
    
    

    
    
if st.session_state.attempts == 5:
    st.write("You won the game! These were your choices:", st.session_state.choices)



if st.button("New game"):
    st.session_state.squares = [True, True, True, True, False]
    shuffle(st.session_state.squares)
    st.session_state.attempts = 0
    st.session_state.choices = []
    st.rerun()
