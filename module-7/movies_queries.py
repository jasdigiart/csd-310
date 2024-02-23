import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}


 
try:
    db = mysql.connector.connect(**config)
    
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...\n")
    
    #This query displays the fields for studio using Select all from studio
    print("--DISPLAYING studio RECORDS--")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    for studio in studios:
       print("Studio ID: {} \nStudio Name: {}\n".format(studio[0],studio[1]))
       
    #This query displays the fields for film genre using Select all from genre   
    print("--DISPLAY genre RECORDS--")   
    cursor = db.cursor()
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    for genre in genres:
       print("Genre ID: {} \nGenre Name: {}\n ".format(genre[0],genre[1]))
       
    #This query displays the fields for film names with a runtime of less than 2 hours
    print("--DISPLAY film RECORDS--")
    cursor = db.cursor()
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <120")
    films = cursor.fetchall()
    for film in films:
       print("Film Name: {} \nRuntime: {}\n".format(film[0],film[1]))
       
     #This query displays the fields for film names and the film director.
    print("--DISPLAY director RECORDS in Order--")
    cursor = db.cursor()
    cursor.execute("SELECT film_name, film_director FROM film")
    films = cursor.fetchall()
    for film in films:
       print("Film Name: {} \nDirector: {}\n".format(film[0], film[1]))
    

    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
        
    else:
        print(err)

finally:
    db.close()
  


