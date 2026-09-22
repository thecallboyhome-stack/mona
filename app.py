import google.generativeai as genai
import streamlit as st

# Page title aur styling
st.set_page_config(
    page_title="Mona - AI Influencer", page_icon="✨", layout="centered"
)

st.title("✨ Meet Mona - Your AI Fashion & Nail Art Influencer")
st.write(
    "Hello! Main Mona hoon. Mujhse fashion, nail art, ya kisi bhi cheez ke baare me baat karein!"
)

# Google Gemini API key configure karein
# (Render par hum ise Environment Variable me daalenge)
import os

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
  st.error(
      "API Key nahi mili! Kripya Render ke Environment Variables me"
      " GEMINI_API_KEY add karein."
  )
else:
  genai.configure(api_key=api_key)

  # AI ka persona (System prompt jisse wo human ki tarah soche aur baat kare)
  system_instruction = (
      "Aap ek 21 saal ki stylish AI fashion aur nail art influencer hain jiska"
      " naam Mona hai. Aap Hindi aur English (Hinglish) me bohot friendly,"
      " aakarshak aur natural tareeqe se baat karti hain. Aap logon ki pasand"
      " samajhti hain aur unhe nail art, styling, aur trends ke baare me best"
      " advice deti hain."
  )

  model = genai.GenerativeModel(
      model_name="gemini-1.5-flash", system_instruction=system_instruction
  )

  # Chat history maintain karne ke liye
  if "messages" not in st.session_state:
    st.session_state.messages = []

  # Purani chat dikhayein
  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  # User se input lena
  if prompt := st.chat_input("Mona se kuch puchiye..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
      st.markdown(prompt)

    # AI ka response generate karna
    try:
      chat = model.start_chat(history=[])
      # Pichli chat ka context bhej kar response lena
      response = model.generate_content(prompt)
      bot_reply = response.text

      with st.chat_message("assistant"):
        st.markdown(bot_reply)
      st.session_state.messages.append(
          {"role": "assistant", "content": bot_reply}
      )
    except Exception as e:
      st.error(f"Kuch error aa gaya: {e}")
