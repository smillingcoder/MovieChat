import mysql.connector
from datetime import date, timedelta


def connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='demo'
    )


def movie_count():
    conn=connection()
    c=conn.cursor()
    query="""select count(*) from Final_Table"""
    c.execute(query)
    count=c.fetchone()[0]
    c.close()
    conn.close()
    return count

def data_insertion(List):
    conn=connection()
    c=conn.cursor()
    query="""INSERT IGNORE INTO Final_Table
    (movie_id,genres,release_date,title,vote_average,overview,poster_path)
    VALUES
    (%s,%s,%s,%s,%s,%s,%s)"""
    c.executemany(query,List)
    conn.commit()
    c.close()
    conn.close()
    print("insertion complete")



def complete_movie_info():
    conn=connection()
    c=conn.cursor()
    query="""SELECT movie_id,genres FROM Final_Table"""
    c.execute(query)
    rows=c.fetchall()
    c.close()
    conn.close()
    return rows

def selected_movie(rows,mood_genres):
    final_list=[]
    for row in rows:
        count=0
        for i in mood_genres:
            if(i in (row[1].strip().split())):
                count+=1
        if(count>1):
            if row[0] not in final_list:
                final_list.append(row[0])

    return final_list

def movies_to_display(final_list):
    conn=connection()
    c=conn.cursor()
    placeholders = ",".join(["%s"] * len(final_list))
    query = f"""
        SELECT movie_id,genres,release_date,title,vote_average,overview,poster_path
        FROM Final_Table
        WHERE movie_id IN ({placeholders})
    """
    c.execute(query, tuple(final_list))
    rows = c.fetchall()
    c.close()
    conn.close()
    return rows



def should_refresh():
    conn = connection()
    c = conn.cursor()

    query = """
    SELECT DATE(CREATE_TIME)
    FROM information_schema.tables
    WHERE table_schema = 'demo'
    AND table_name = 'Final_Table'
    """
    c.execute(query)
    created_on = c.fetchone()[0]

    c.close()
    conn.close()

    if created_on is None:
        return True

    return date.today() >= created_on + timedelta(days=10)


def update_table():
    conn = connection()
    c = conn.cursor()
    c.execute("TRUNCATE TABLE Final_Table")
    conn.comit()
    c.close()
    conn.close()


