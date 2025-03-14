import streamlit as st
from random import shuffle, choice

"""
# GOAL MINE
Probability of winning the game
"""

if "squares" not in st.session_state:
    st.session_state.squares = [True, True, True, True, False] 
    shuffle(st.session_state.squares)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "choices" not in st.session_state:
    st.session_state.choices = []  

if "goal_step" not in st.session_state:
    st.session_state.goal_step = False  # Nuova fase: tiro in porta

if "goalkeeper_choice" not in st.session_state:
    st.session_state.goalkeeper_choice = None

if "show_goalkeeper_choice" not in st.session_state:
    st.session_state.show_goalkeeper_choice = False

st.write("Squares sequence:") 
st.write(st.session_state.squares)

if not st.session_state.goal_step:
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
            st.write(f"Attempt {st.session_state.attempts + 1}: You have been thwarted, you lost possession of the ball!")
            st.write("Press on new game if you want to start a new match")
            st.session_state.goal_step = False
    
    if st.session_state.attempts == 5:
        st.session_state.goal_step = True
        st.session_state.goalkeeper_choice = choice(["Bottom Left", "Top Left", "Center", "Bottom Right", "Top Right"])
        st.rerun()
else:
    st.write("You are in front of the goalkeeper, choose where to shoot")
    shot_options = ["Bottom Left", "Top Left", "Center", "Bottom Right", "Top Right"]
    
    
    st.session_state.show_goalkeeper_choice = st.checkbox("Show goalkeeper's choice")
    if st.session_state.show_goalkeeper_choice:
        st.write(f"Goalkeeper will dive to: {st.session_state.goalkeeper_choice}")
    
    chosen_shot = st.radio("Select your shot", shot_options)
    
    if st.button("Shoot!"):
        if chosen_shot == st.session_state.goalkeeper_choice:
            st.write(f"The goalkeeper guessed your shot ({st.session_state.goalkeeper_choice})! You missed!")
        else:
            st.write(f"Goal!!! You shot at {chosen_shot} and the goalkeeper went {st.session_state.goalkeeper_choice}!")
        
        st.session_state.goal_step = False  # Reset partita
        st.session_state.attempts = 0
        st.session_state.choices = []
        st.session_state.squares = [True, True, True, True, False]
        shuffle(st.session_state.squares)

if st.button("New game"):
    st.session_state.squares = [True, True, True, True, False]
    shuffle(st.session_state.squares)
    st.session_state.attempts = 0
    st.session_state.choices = []
    st.session_state.goal_step = False
    st.session_state.goalkeeper_choice = None
    st.session_state.show_goalkeeper_choice = False
    st.rerun()
