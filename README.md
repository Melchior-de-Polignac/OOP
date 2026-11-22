# OOP

My solutions to the OOP course exercises (ISDS51040), written to revise for the exam.

- `01` and `02`: UML decks (PDF and PPTX)
- `03` to `12`: OOP notebooks and design patterns
- `13`: SQL company database
- `14`: pytest exercise
- `15`: port scanner
- `16`: FastAPI students API
- `17`: bash install script
- `19`: git mini exercise

Most files run on their own:

```bash
python 06_factory/payments.py
```

Tests:

```bash
pip install pytest pytest-mock
pytest
```

SQL:

```bash
cd 13_sql_company_db
sqlite3 company.db < schema.sql
sqlite3 company.db < data.sql
sqlite3 company.db < queries.sql
```

API:

```bash
pip install -r 16_api/requirements.txt
uvicorn students_api:app --app-dir 16_api --reload
```
