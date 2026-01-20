import requests
import time
import os


def tmdb_process():
    
    with open("key.txt","r") as f:
        TOKEN=f.read()
    
    header={
        "Authorization":f"Bearer {TOKEN}",
        "accept":"application/json"
    }
    URL="https://api.themoviedb.org/3/movie/popular"
    movies_in_dict=[]
    for page in range(1,51):
        for attempt in range(3):
            try:
                response=requests.get(url=URL,headers=header,
                                      params={"page":page,"region": "IN"},
                                      timeout=30).json()
                movies_in_dict.extend(response['results'])
                print(f"page-{page}")
                break
            except Exception as e:
                print(f"error on page{page}, retrying...attempt{attempt}")
                time.sleep(2)

        genre_name = { 28: "Action", 
            12: "Adventure", 
            16: "Animation", 
            35: "Comedy", 
            80: "Crime", 
            99: "Documentary", 
            18: "Drama", 
            10751: "Family", 
            14: "Fantasy", 
            36: "History", 
            27: "Horror", 
            10402: "Music", 
            9648: "Mystery", 
            10749: "Romance", 
            878: "Science Fiction", 
            10770: "TV Movie", 
            53: "Thriller", 
            10752: "War", 
            37: "Western" 
            }
        
        movies_tuple=[]
        for movie in movies_in_dict:
            genre_ids=movie['genre_ids']
            genres=" ".join(str(genre_name[n]) for n in genre_ids)
            movies_tuple.append((movie.get('id'),
                                genres,
                                movie.get('release_date'),
                                movie.get('title'),
                                movie.get('vote_average'),
                                movie.get('overview'),
                                movie.get('poster_path')))
    return movies_tuple
            

