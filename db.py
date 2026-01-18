import mysql.connector

def database_setup():
    def connection():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='demo'
        )
    conn=connection()
    c=conn.cursor()
    querry="""create table if not exists Final_Table(
        id INT PRIMARY KEY AUTO_INCREMENT,
        movie_id BIGINT NOT NULL UNIQUE,
        genres TEXT,
        release_date DATE,
        title VARCHAR(255),
        vote_average DECIMAL(2,1),
        overview TEXT,
        poster_path VARCHAR(255) DEFAULT NULL
        )"""

    c.execute(querry)

    conn.commit()
    c.close()
    connection().close()
    print("database present")




