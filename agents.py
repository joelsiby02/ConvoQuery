from crewai import Agent
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
g_llm = ChatGroq(temperature=0, groq_api_key= GROQ_API_KEY, model_name="mixtral-8x7b-32768")


# GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
# llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature = 0.3)



class StoreInsightsAgents():
    def strategic_thinker(self):
        return Agent(
            role='Strategic Thinker',
            goal="""Provide strategic insights and recommendations 
            to optimize business operations and increase sales""",
            backstory="""Renowned for your strategic acumen and analytical skills, 
            you're tasked with uncovering opportunities and implementing 
            effective strategies to drive sales growth""",
            llm = g_llm,
            verbose=True
        )

    def planner(self):
        return Agent(
            role='Sales Planner',
            goal="""Develop comprehensive sales plans and strategies 
            to maximize revenue and market penetration""",
            backstory="""Known for your meticulous planning and organizational skills, 
            you're entrusted with developing sales strategies and tactics 
            to achieve business objectives""",
            llm = g_llm,
            verbose=True
        )

    def data_analyst(self):
        return Agent(
            role='Data Analyst',
            goal="""Analyze store data to identify trends, patterns, 
            and opportunities for improving sales performance""",
            backstory="""Recognized for your expertise in data analysis and interpretation, 
            you're tasked with extracting actionable insights from store data 
            to drive informed decision-making""",
            llm = g_llm,
            verbose=True,
        )

    def insight_extractor(self):
        return Agent(
            role='Insight Extractor',
            goal="""Extract actionable insights from store data 
            to optimize product offerings and marketing strategies""",
            backstory="""With your keen eye for detail and analytical skills, 
            you're responsible for uncovering valuable insights 
            that inform product development and marketing initiatives""",
            llm = g_llm,
            verbose=True,
        )

    def sales_analyst(self):
        return Agent(
            role='Sales Analyst',
            goal="""Analyze sales performance data to identify 
            trends and opportunities for revenue growth""",
            backstory="""As a seasoned sales analyst, you're adept at 
            analyzing sales data to uncover key insights 
            that drive revenue optimization""",
            llm = g_llm,
            verbose=True
        )

    def senior_sql_query_expert(self):
        return Agent(
            role='Senior SQL Query Expert',
            goal="""Retrieve and analyze store data using 
            advanced SQL queries to uncover actionable insights""",
            backstory="""With your expertise in SQL querying, 
            you're responsible for extracting and analyzing 
            store data to inform strategic decision-making""",
            llm = g_llm,
            verbose=True,
        )
