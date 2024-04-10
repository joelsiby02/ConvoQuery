# Importing necessary libraries
from dotenv import load_dotenv
import streamlit as st

# Loading environment variables from .env file
load_dotenv()

# Configuring page title and icon
st.set_page_config(page_title="CQ", page_icon=":speech_balloon:")

# App title
st.title("ConvoQuery")

# Importing a function to connect to the database URI
from langchain_community.utilities import SQLDatabase

# Function to initialize the database connection
def init_db(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
    db_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri, sample_rows_in_table_info=3)

# Sidebar for database connection settings
with st.sidebar:
    st.subheader("Setting")
    st.write("Connect to your Database and start chatting / draw insights with it 😊")
    
    st.text_input("Host", value="localhost", key="Host")
    st.text_input("Port", value="3306", key="Port")
    st.text_input("User", value="root", key="User")
    st.text_input("Password", type="password", key="Password")
    st.text_input("Database", value='atliq_tshirts', key="Database")
    
    connect_button = st.button("Connect")  # Button to trigger database connection

# Attempting to connect to the database if the Connect button is clicked
if connect_button:
    # Show a spinner while connecting
    with st.spinner("Connecting to the database..."):
        # Initializing the database connection
        db = init_db(
            st.session_state['User'],
            st.session_state['Password'],
            st.session_state['Host'],
            st.session_state['Port'],
            st.session_state['Database']
        )
        st.session_state.db = db
        st.success("Connected to the database successfully")

# Importing message classes for chat interface
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Initializing chat history if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hey I'm Lora, I'm your SQL assistant, Ask me anything related to your DataBase.")
    ]

# Displaying messages in the chat interface
for msg in st.session_state.chat_history:
    if isinstance(msg, AIMessage):
        with st.chat_message("Lora"):
            st.markdown(msg.content)
    elif isinstance(msg, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(msg.content)

# Input field for user queries
user_query = st.chat_input("Type a message...")
if user_query is not None and user_query.strip() != "":
    # Appending user query to chat history
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    
    # Displaying user query in the chat interface
    with st.chat_message("Human"):
        st.markdown(user_query)
