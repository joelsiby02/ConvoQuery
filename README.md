# ConvoQuery - An app Designed for StoreManagers

This application allows users to query a database containing information about their database, including their brands, colors, sizes, prices,stock quantities as well as their Business insigts

## Installation

1. Clone this repository to your local machine:

   ```
   git clone (https://github.com/joelsiby02/ConvoQuery.git)
   ```

2. Navigate to the project directory:

   ```
   cd ConvoQuery
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set up the environment variables by creating a `.env` file in the project root directory and adding the following variables:

   ```
   DB_USER=<database_username>
   DB_PASSWORD=<database_password>
   DB_HOST=<database_host>
   DB_NAME=<database_name>
   GOOGLE_API_KEY=<your_google_api_key> "https://makersuite.google.com/"

   !!! #replace with your database's and llm key !!!
   ```

2. Run the application:

   ```
   streamlit run app.py
   ```

3. Access the application in your web browser at `http://localhost:5000`.

4. Enter your query in the text input field and click the "Submit" button to execute the query.

## Example Queries

- To retrieve the price of a small size Adidas white T-shirt:
  ```
  What is the cost of a small size Adidas White T-Shirt?
  ```

- To list all available T-shirt brands:
  ```
  Print all brand names from t_shirts?
  ```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This Project is designed as Team6 mini Project
