from langchain_community.utilities.sql_database import SQLDatabase
from langchain import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
# from langchain.chains import SQLDatabaseSequentialChain
import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.llms import CTransformers
from ctransformers import AutoModelForCausalLM

from mistral import create_text_generation_pipeline

# Load environment variables from .env file
load_dotenv()

# Google Palm LLM Setup
# llm = GooglePalm(google_api_key=os.getenv('GOOGLE_API_KEY'), temperature=0.2)

pipeline = create_text_generation_pipeline()
llm = HuggingFacePipeline(
    pipeline=pipeline,
    )


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