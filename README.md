
# TEXT_TO_SQL

This project aims to develop a robust Text-to-SQL engine using OpenAI's GPT-4 model. The engine converts natural language queries into SQL queries, enabling seamless interaction with databases through natural language.




## Key Features

- GPT-4 Integration: Utilizes OpenAI's GPT-4 model to interpret natural language questions and generate accurate SQL queries.
- SQL Validation: Leverages the sqlglot library to validate the syntax of generated SQL queries.
- Benchmarking: Evaluates the engine's performance using the BIRD benchmark's test dataset to ensure accuracy and efficiency.


## Deployment

To deploy this project run

```bash
  source VIRENV/bin/activate
```
```bash
  pip install -r requirements.txt
```
```bash
  python3 app.py
```

