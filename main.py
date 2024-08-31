import sqlite3
import json
import openai
import sqlglot
import os
import random
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Paths to your SQLite database files, mapped by db_id
database_paths = {
    'california_schools': '/DATABASE/california_school.sqlite',
    'card_games': 'DATABASE/card_games.sqlite',
    'codebase_community': 'DATABASE/codebase_community.sqlite',
    'european_football': 'DATABASE/european_football_2.sqlite',
    'financial': 'DATABASE/financial.sqlite',
    'formula_1': 'DATABASE/formula_1.sqlite',
    'student_club': 'DATABASE/student_club.sqlite',
    'superhero': 'DATABASE/superhero.sqlite',
    'thrombosis_prediction': 'DATABASE/thrombosis_prediction.sqlite',
    'toxicology': 'DATABASE/toxicology.sqlite',
    'debit_card_specializing' : 'DATABASE/debit_card_specializing'
    # Add paths for all your 11 databases
}

# Load the BIRD benchmark JSON file
with open('dev.json', 'r') as file:
    benchmark_data = json.load(file)

# Function to validate and execute SQL queries
def validate_and_execute_sql(query, db_id):
    try:
        # Validate SQL syntax using sqlglot
        parsed_query = sqlglot.parse_one(query, read='sqlite')
        print(f"Validated SQL Query: {parsed_query}")
        
        # Connect to the correct database
        conn = sqlite3.connect(database_paths[db_id])
        cursor = conn.cursor()
        
        # Execute the query
        cursor.execute(parsed_query)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        print(f"SQL Execution Error: {e}")
        return str(e)

# Function to generate SQL query from a natural language question
def generate_sql_from_question(question):
    prompt = [
        """
        You are an expert in converting English questions to SQL queries. The SQL database has various tables with specific columns. 
        Your task is to convert the following English question into a valid SQL query. 
        The SQL query should not have backticks or the word 'SQL' in it. Only return the SQL query.
        Examples:
        - How many entries of records are present? 
          SQL: SELECT COUNT(*) FROM table_name;
        - Tell me all the users living in India? 
          SQL: SELECT * FROM users WHERE country="India";
        """
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt[0]},
            {"role": "user", "content": f"Question: {question}\n\nSQL:"}
        ],
        max_tokens=150
    )
    generated_sql = response.choices[0].message['content'].strip()
    return generated_sql

# Function to evaluate the text-to-SQL engine using the BIRD benchmark
def evaluate_benchmark():
    success_count = 0
    random_entries = random.sample(benchmark_data, 30)
    
    for entry in random_entries:
        question = entry['question']
        expected_sql = entry['SQL']
        db_id = entry['db_id']  # Get the database ID for this question

        # Generate SQL using the LLM
        generated_sql = generate_sql_from_question(question)

        # Validate and execute the generated SQL on the correct database
        generated_result = validate_and_execute_sql(generated_sql, db_id)

        # Validate and execute the expected SQL on the correct database
        expected_result = validate_and_execute_sql(expected_sql, db_id)

        # Compare the results
        if generated_result == expected_result:
            success_count += 1
            print(f"Question ID {entry['question_id']}: Success")
            print(f"Generated SQL: {generated_sql}")
            print(f"Generated Result: {generated_result}")
            print(f"Expected SQL: {expected_sql}")
            print(f"Expected Result: {expected_result}\n")
        else:
            print(f"Question ID {entry['question_id']}: Failure")
            print(f"Generated SQL: {generated_sql}")
            print(f"Generated Result: {generated_result}")
            print(f"Expected SQL: {expected_sql}")
            print(f"Expected Result: {expected_result}\n")

    success_rate = (success_count / 30) * 100
    print(f"Success Rate: {success_rate}%")

if __name__ == "__main__":
    evaluate_benchmark()
    
