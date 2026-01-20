from flask import Flask,render_template,request
import threading
from db import database_setup
from fetch_tmdb import tmdb_process
from Queries import data_insertion,complete_movie_info,selected_movie,movies_to_display,movie_count,should_refresh,update_table
from nlp_model import bot_mood
from mood_to_genres_map import genres_for_query


app=Flask(__name__)

DATA_READY=False
startup_started = False


@app.route("/",methods=["GET","POST"])
def home():
    global DATA_READY
    reply=None
    final_movies = []
    mood_genres=[]
    mood_dict = {"label": ""}
    user=request.form.get("user","").strip()
    if request.method=="POST":
        if not DATA_READY:
            reply=f"⏳Database is still setting up. Please try again in a moment.{DATA_READY}"
            return render_template("index.html",reply=reply)
        if user:
            mood_dict=bot_mood(user)
            mood_genres=genres_for_query(mood_dict)
            rows=complete_movie_info()
            selected_rows=selected_movie(rows,mood_genres)
            final_movies=movies_to_display(selected_rows)
            if not final_movies:
                reply="enter a valid text"
            else:reply=final_movies
        else:
            reply="enter something..."

    return render_template("index.html",reply=reply,
                            total_movies=movie_count(),
                            total_results=len(final_movies),
                            your_mood=mood_dict['label'],
                            genres=mood_genres)

def initialize():
    global DATA_READY

    DATA_READY=False
    database_setup()

    if should_refresh() or  not movie_count():
        update_table()
        data_insertion(tmdb_process())
    DATA_READY=True


@app.before_request
def start_background_task():
    global startup_started

    if not startup_started:
        startup_started = True

        thread = threading.Thread(target=initialize)
        thread.daemon = True
        thread.start()




if (__name__)==("__main__"):
    app.run(debug=True,use_reloader=False)



