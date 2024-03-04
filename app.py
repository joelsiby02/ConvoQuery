from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from langchain.prompts.prompt import PromptTemplate
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Google Palm LLM Setup
llm = GooglePalm(google_api_key=os.getenv('GOOGLE_API_KEY'), temperature=0.2)

# Database Setup
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=3)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# Streamlit UI
def main():
    st.title("ConvoQuery")
    # User Input for the Question
    question = st.text_input("Enter your question:")

    if st.button("Submit"):
        if question:
            st.text("User: " + question)

            # Execute the LangChain interaction
            response = db_chain.run(question)

            st.text("Database: " + response)

if __name__ == "__main__":
    main()
