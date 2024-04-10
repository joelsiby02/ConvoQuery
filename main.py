from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import streamlit as st

# Function to initialize the database connection
def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
    db_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)

def get_sql_chain(db):
    template = """
    You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
    Based on the table schema below, write a SQL query that would answer the user's question. Take the conversation history into account.
    
    <SCHEMA>{schema}</SCHEMA>
    
    Conversation History: {chat_history}
    
    Write only the SQL query and nothing else. Do not wrap the SQL query in any other text, not even backticks.
    
    For example:
    Question: which 3 artists have the most tracks?
    SQL Query: SELECT ArtistId, COUNT(*) as track_count FROM Track GROUP BY ArtistId ORDER BY track_count DESC LIMIT 3;
    Question: Name 10 artists
    SQL Query: SELECT Name FROM Artist LIMIT 10;
    
    Your turn:
    
    Question: {question}
    SQL Query:
    """
    
    prompt = ChatPromptTemplate.from_template(template)
  
    llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0.3)
  
    def get_schema(_):
        return db.get_table_info()
    
    return (
        RunnablePassthrough.assign(schema=get_schema)
        | prompt
        | llm
        | StrOutputParser()
    )

def get_response(user_query: str, db: SQLDatabase, chat_history: list):
    sql_chain = get_sql_chain(db)
    
    template = """
    You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
    Based on the table schema below, question, sql query, and sql response, write a natural language response.
    <SCHEMA>{schema}</SCHEMA>

    Conversation History: {chat_history}
    SQL Query: <SQL>{query}</SQL>
    User question: {question}
    SQL Response: {response}
    
    I will provide you with an example how i am expecting the output to be:
    User question: What's the name of my DataBase?
    SQL Query: SELECT DATABASE();
    SQL Response: Hey there, the name of your Database is atliq_store, the SQL query used to fetch the response is SELECT DATABASE();
    
    I want to mandatorily maintain the response in this format for whatever question user asks!
    """

    prompt = ChatPromptTemplate.from_template(template)
  
    llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0)
  
    chain = (
        RunnablePassthrough.assign(query=sql_chain).assign(
            schema=lambda _: db.get_table_info(),
            response=lambda vars: db.run(vars["query"]),
        )
        | prompt
        | llm
        | StrOutputParser()
    )
  
    output = chain.invoke({
        "question": user_query,
        "chat_history": chat_history,
    })

    # Extract only the relevant response content
    response_content = output.split('\n')[-1]  # Extract the last line
    return response_content

# Initialize chat history if not present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello! I'm Lora, your Database AI Assistant. Ask me anything about your database..."),
    ]

load_dotenv()

st.set_page_config(page_title="CQ", page_icon=":speech_balloon:")

st.title("ConvoQuery")

# Sidebar for database connection settings
with st.sidebar:
    st.subheader("Setting")
    st.write("Connect to your Database and start chatting / draw insights with it 😊")
    
    st.text_input("Host", value="localhost", key="Host")
    st.text_input("Port", value="3306", key="Port")
    st.text_input("User", value="root", key="User")
    st.text_input("Password", type="password", key="Password")
    st.text_input("Database", value='atliq_tshirts', key="Database")
    
    if st.button("Connect"):
        with st.spinner("Connecting to database..."):
            db = init_database(
                st.session_state["User"],
                st.session_state["Password"],
                st.session_state["Host"],
                st.session_state["Port"],
                st.session_state["Database"]
            )
            st.session_state.db = db
            st.success("Connected to database!")

# Display chat history
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("Lora"):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)

# Collect user input
user_query = st.chat_input("Type a message...")
if user_query is not None and user_query.strip() != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    
    with st.chat_message("Human"):
        st.markdown(user_query)
        
    with st.chat_message("Lora"):
        response = get_response(user_query, st.session_state.db, st.session_state.chat_history)
        st.markdown(response)
        
    st.session_state.chat_history.append(AIMessage(content=response))
