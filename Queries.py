from db import connection
from datetime import datetime, timedelta



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
    query="""INSERT OR IGNORE INTO Final_Table
    (movie_id,genres,release_date,title,vote_average,overview,poster_path)
    VALUES
    (?,?,?,?,?,?,?)"""
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
    placeholders = ",".join(["?"] * len(final_list))
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



def update_table():
    conn=connection()
    c=conn.cursor()

    query=""" DELETE FROM Final_Table"""
    c.execute(query)
    conn.commit()
    c.close()
    conn.close()


def date_check():

    conn=connection()
    c=conn.cursor()

    query=""" SELECT DOI FROM Final_Table ORDER BY id LIMIT 1"""
    c.execute(query)

    row=c.fetchone()
    c.close()
    conn.close()

    now=datetime.now()

    if not row or not row[0]:
        return True

    doi = datetime.fromisoformat(row[0])

    return now - doi > timedelta(days=15)




def search_movie_by_title(title):

    conn = connection()
    c = conn.cursor()

    query = """
    SELECT movie_id, genres, release_date, title, vote_average, overview, poster_path
    FROM Final_Table
    WHERE LOWER(title) LIKE LOWER(?)
    """

    search_value = "%" + title + "%"

    c.execute(query, (search_value,))
    rows = c.fetchall()

    c.close()
    conn.close()

    return rows

