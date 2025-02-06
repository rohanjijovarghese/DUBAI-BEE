from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st


load_dotenv()

client = OpenAI()

# training the ai is done here
initial_message=[  
        {"role": "system", "content": "You are a trip planner to dubai. You are an expert in dubai tourism,location,food,events,transportation.You are able to guide users to plan their vaccation to dubai.You should respond proffessionally.Your name is Dubai bee.Short name DB.Respomse should be 200 or less words.Always ask questions to user and help them plan the trip.give the user the daywise plans and tips.everything must be short and simple responses"},
        {
            "role": "assistant",
            "content": "Helloo I am DB, your expert Trip planner, How can i help you? ."
        }

]

# created function to get respose llm (response from ai)
def response_from_llm(messages):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
    )

    return completion.choices[0].message


if "messages" not in st.session_state:
    st.session_state.messages = initial_message 


st.title("DUBAI BEE - Dubai trip planner AI")

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

user_message = st.chat_input("Enter your message")

if user_message:
    new_message={
            "role": "user",
            "content": user_message
        }
    st.session_state.messages.append(new_message)
    with st.chat_message(new_message["role"]):
        st.markdown(new_message["content"])
    response=response_from_llm(st.session_state.messages)
    if response:
        response_message={
            "role": "assistant",
            "content": response.content
        }
        st.session_state.messages.append(response_message)
        with st.chat_message(response_message["role"]):
            st.markdown(response_message["content"])



