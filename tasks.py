from crewai import Task
from textwrap import dedent

class StoreInsightsTasks():
    def financial_analysis(self, agent):
        return Task(
            description=dedent(f"""
                Conduct a thorough analysis of the store's financial performance 
                and market trends. This includes examining key financial metrics 
                such as revenue growth, profit margins, inventory turnover, 
                and return on investment.

                Your analysis should also consider market dynamics, 
                customer behavior trends, and competitive landscape.

                Provide actionable insights and recommendations 
                to optimize sales and enhance profitability.

                Ensure your analysis is based on the most recent data available.
            """),
            expected_output="Provide actionable insights and recommendations to optimize sales and enhance profitability.",
            agent=agent
        )

    def sales_forecasting(self, agent):
        return Task(
            description=dedent(f"""
                Develop sales forecasts for the upcoming quarter based 
                on historical sales data, market trends, and external factors 
                such as seasonality and economic conditions.

                Utilize statistical forecasting methods and predictive analytics 
                to generate accurate and reliable forecasts.

                Provide a comprehensive analysis of the factors influencing 
                sales performance and potential areas for improvement.

                Present your sales forecast report with clear insights 
                and actionable recommendations.
            """),
            expected_output="Present a comprehensive sales forecast report with clear insights and actionable recommendations.",
            agent=agent
        )

    def customer_segmentation(self, agent):
        return Task(
            description=dedent(f"""
                Conduct customer segmentation analysis to identify 
                distinct customer segments based on demographic, 
                behavioral, and psychographic characteristics.

                Utilize clustering algorithms and data mining techniques 
                to group customers into meaningful segments.

                Provide insights into the unique needs, preferences, 
                and purchasing behaviors of each customer segment.

                Develop targeted marketing strategies and personalized 
                promotional campaigns to effectively engage 
                each customer segment.
            """),
            expected_output="Develop targeted marketing strategies and personalized promotional campaigns to effectively engage each customer segment.",
            agent=agent
        )

    def product_recommendation(self, agent):
        return Task(
            description=dedent(f"""
                Develop personalized product recommendations 
                for customers based on their past purchase history, 
                browsing behavior, and demographic profile.

                Utilize machine learning algorithms and collaborative 
                filtering techniques to generate accurate 
                and relevant product recommendations.

                Implement recommendation systems across various 
                channels, including e-commerce platforms, 
                email marketing campaigns, and personalized 
                product recommendations.

                Monitor and evaluate the effectiveness of 
                product recommendation strategies 
                and iterate based on customer feedback 
                and performance metrics.
            """),
            expected_output="Implement recommendation systems across various channels, including e-commerce platforms, email marketing campaigns, and personalized product recommendations.",
            agent=agent
        )

    def competitor_analysis(self, agent):
        return Task(
            description=dedent(f"""
                Conduct a comprehensive analysis of key competitors 
                in the retail industry, including their market 
                positioning, product offerings, pricing strategies, 
                and customer engagement tactics.

                Utilize competitive intelligence tools and 
                market research techniques to gather 
                relevant data on competitors' performance 
                and market share.

                Identify competitive strengths and weaknesses 
                and assess potential threats and opportunities 
                posed by competitors.

                Develop strategic recommendations to 
                strengthen the store's competitive advantage 
                and capture market opportunities.
            """),
            expected_output="Develop strategic recommendations to strengthen the store's competitive advantage and capture market opportunities.",
            agent=agent
        )

    def sales_performance_analysis(self, agent):
        return Task(
            description=dedent(f"""
                Analyze sales performance data to evaluate 
                the effectiveness of marketing campaigns, 
                promotions, and sales strategies.

                Utilize key performance indicators (KPIs) 
                such as sales growth, customer acquisition, 
                and retention rates to assess sales performance.

                Identify trends, patterns, and insights 
                to optimize sales and marketing efforts.

                Develop actionable recommendations 
                to improve sales performance and achieve 
                revenue targets.
            """),
            expected_output="Develop actionable recommendations to improve sales performance and achieve revenue targets.",
            agent=agent
        )
        
    def handle_user_query(self, agent):
        return Task(
            description=dedent(f"""
                As the database query agent, your task is to handle user queries 
                about the database schema and execute SQL queries accordingly.

                If a user asks a question related to the database, 
                interpret the query and execute the corresponding SQL query 
                against the database.

                Provide the user with the requested information along with 
                the executed SQL query for transparency and clarity.

                Ensure that you understand the database schema and can 
                effectively navigate and query the database to retrieve 
                the requested information.
            """),
            expected_output="Provide the requested information along with the executed SQL query for transparency and clarity.",
            agent=agent
        )
