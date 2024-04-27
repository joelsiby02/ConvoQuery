from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import HumanMessagePromptTemplate
from langchain.schema import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv
load_dotenv()


# Access the environmental variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

llm = ChatGroq(temperature=0, groq_api_key= GROQ_API_KEY, model_name="mixtral-8x7b-32768")

host = DB_HOST
port = DB_PORT
username = DB_USER
password = DB_PASSWORD
database_schema = DB_NAME
mysql_uri = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_schema}"

db = SQLDatabase.from_uri(mysql_uri, include_tables=['orders'],sample_rows_in_table_info=2)

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

def retrieve_from_db(query: str) -> str:
    db_context = db_chain(query)
    db_context = db_context['result'].strip()
    return db_context

def generate(query: str) -> str:
    db_context = retrieve_from_db(query)
    
    system_message = """You are a professional representative of an employment agency.
        You have to answer user's queries and provide relevant information to help in their job search. 
        Example:
        
        Input:
        What are the T-shirt brands we sell?
        
        Context:
        The brands we sell are:
        1. Nike
        2. Adidas
        3. Levi
        4. Van Hussen
        
        Output:
        The Brands we sell here are Nike, Adidas, Levi, Van Hussen
        """
    
    human_qry_template = HumanMessagePromptTemplate.from_template(
        """Input:
        {human_input}
        
        Context:
        {db_context}
        
        Output:
        """
    )
    messages = [
      SystemMessage(content=system_message),
      human_qry_template.format(human_input=query, db_context=db_context)
    ]
    response = llm(messages).content
    return response

generate("email id of the customer 887")
