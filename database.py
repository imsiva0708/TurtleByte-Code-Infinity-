from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://sql6687929:wbLGBqwhfu@sql6.freesqldatabase.com/sql6687929?charset=utf8mb4")

with engine.connect() as conn:
    result = conn.execute(text("select * from dailystats"))
    result_as_dict = result.mappings().all()