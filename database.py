from sqlalchemy import create_engine, text


engine = create_engine("mysql+pymysql://sql6687929:wbLGBqwhfu@sql6.freesqldatabase.com/sql6687929?charset=utf8mb4")

def load_from_db():
    with engine.connect() as conn:
            result = conn.execute(text("select * from dailystats"))
            result_as_dict = result.mappings().all()
            return result_as_dict
def add_to_db(data,name):
    with engine.connect() as conn:
         query = f"INSERT INTO dailystats (username,steps,calories,workout_time) VALUES ({name}, {data['steps']}, {data['calories']}, {data['workout_time']});"