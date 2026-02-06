import pandas as pd
from sqlalchemy import create_engine

DB_URL = "postgresql://neondb_owner:npg_a2cfwEmDp5ig@ep-noisy-grass-ai9zgc4l-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require"

try:
    engine = create_engine(DB_URL)
    df = pd.read_sql_query("SELECT start_date FROM employees", engine)
    print(f"Total Rows: {len(df)}")
    if not df.empty:
        df['start_date'] = pd.to_datetime(df['start_date'])
        print(f"Min Date: {df['start_date'].min()}")
        print(f"Max Date: {df['start_date'].max()}")
        print("Year Counts:")
        print(df['start_date'].dt.year.value_counts().sort_index())
    else:
        print("DataFrame is empty.")
except Exception as e:
    print(f"Error: {e}")
