import os
from crewai import Crew
from textwrap import dedent
from agents import StoreInsightsAgents
from tasks import StoreInsightsTasks
from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to initialize the database connection
def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
    db_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)

def run():
    # Initialize the database connection using environment variables
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    db_port = "3306"  # Assuming default port

    # Initialize the database connection
    db = init_database(db_user, db_password, db_host, db_port, db_name)

    agents = StoreInsightsAgents()
    tasks = StoreInsightsTasks()

    strategic_thinker_agent = agents.strategic_thinker()
    planner_agent = agents.planner()
    insight_extractor_agent = agents.insight_extractor()
    sales_analyst_agent = agents.sales_analyst()
    senior_sql_query_expert_agent = agents.senior_sql_query_expert()

    financial_analysis_task = tasks.financial_analysis(agent=strategic_thinker_agent)
    sales_forecasting_task = tasks.sales_forecasting(agent=planner_agent)
    customer_segmentation_task = tasks.customer_segmentation(agent=insight_extractor_agent)
    product_recommendation_task = tasks.product_recommendation(agent=sales_analyst_agent)
    competitor_analysis_task = tasks.competitor_analysis(agent=sales_analyst_agent)
    handle_user_query_task = tasks.handle_user_query(agent=senior_sql_query_expert_agent)

    crew = Crew(
        agents=[
            strategic_thinker_agent,
            planner_agent,
            insight_extractor_agent,
            sales_analyst_agent,
            senior_sql_query_expert_agent
        ],
        tasks=[
            financial_analysis_task,
            sales_forecasting_task,
            customer_segmentation_task,
            product_recommendation_task,
            competitor_analysis_task,
            handle_user_query_task
        ],
        verbose=True,
        database=db  # Pass the initialized database connection to Crew
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
    run()
