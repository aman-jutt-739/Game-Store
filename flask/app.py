from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Ahmad123"
app.config["MYSQL_DB"] = "gamestore"

mysql = MySQL(app)
CORS(app)
# @app.route("/")
# def hello_world():

#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM games")
#     data = cur.fetchall()
#     return str(data)

@app.route("/games")
def get_games():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from games")
    rowsgames = cur.fetchall()
   
    # Convert DB rows into a list of dicts
    games = []
    for row in rowsgames:
        cur.execute(f"Select url from footage where game_id = {row[0]}")
        rowsfootage = cur.fetchall()
        game = {
            "id": row[0],
            "name": row[1],
            "surname": row[2],
            "price": float(row[3]),
            "desc": row[4],
            "link": row[5],
            "release": row[6],
            "platforms": row[7],
            "genre": row[8],
            "developers": row[9],
            "publishers": row[10],
            "inCart": row[11],
            "selected": row[12],
            "isHovered": row[13],
            "isLiked": row[14],
            "rating": row[15],
            
            "cover": row[16],
            "footage": [
              rowsfootage[0],
              rowsfootage[1],
              rowsfootage[2],
            ]
        }
        games.append(game)

    return jsonify(games)
@app.route("/gamesfilter")
def get_games_filter():
    filtername = request.args.get('filter', default='', type=str)
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * from games where genre = '{filtername}'")
    rowsgames = cur.fetchall()
   
    # Convert DB rows into a list of dicts
    games = []
    for row in rowsgames:
        cur.execute(f"Select url from footage where game_id = {row[0]}")
        rowsfootage = cur.fetchall()
        game = {
            "id": row[0],
            "name": row[1],
            "surname": row[2],
            "price": float(row[3]),
            "desc": row[4],
            "link": row[5],
            "release": row[6],
            "platforms": row[7],
            "genre": row[8],
            "developers": row[9],
            "publishers": row[10],
            "inCart": row[11],
            "selected": row[12],
            "isHovered": row[13],
            "isLiked": row[14],
            "rating": row[15],
            
            "cover": row[16],
            "footage": [
              rowsfootage[0],
              rowsfootage[1],
              rowsfootage[2],
            ]
        }
        games.append(game)

    return jsonify(games)
if __name__ == "__main__":
    app.run(debug=True)









#  games = {
#         "name": "Cyberpunk 2077",
#         "surname": "cyberpunk",
#         "price": "59.99",
#         "desc": 'Cyberpunk 2077 is a continuation of the events of Cyberpunk 2020, taking an alternate path to that of Cyberpunk V3.0. The game is set in the dystopian metropolis of Night City. It is set in the Free State of Northern California. Night City is located south of San Francisco around the area of Morro Bay, CA. During Cyberpunk 2020, Night City is said to have a population of more than five million inhabitants. However, this number is suspected to be considerably larger in 2077. Following an economic collapse sometime during the early 21st century, the United States is forced to rely on large corporations to survive. These corporations deal in a wide range of areas, such as weapons, robotics, cybernetics, pharmaceuticals, communications, and biotechnology; many of these companies operate above the law. The game follows the story of V — a hired gun on the rise in Night City, the most violent and dangerous metropolis of the corporate-ruled future. A robust character creator will allow players to choose Vs gender, visual appearance, as well as historical background — all of which may influence the shape of the game. The world is inspired by the works of authors such as William Gibson (author of Neuromancer) and Phillip K Dick, whose novel Do Androids Dream of Electric Sheep? and subsequent movie adaption Blade Runner heavily influenced the creator, Mike Pondsmith, in creating the original tabletop RPG.',
#         "link": 'https://www.cyberpunk.net/',
#         "release": '10th of December, 2020',
#         "platforms": 'Playstation 4, PC, Xbox Series S/X, Playstation 5, Xbox One',
#         "genre": 'RPG',
#         "developers": 'CD PROJECT RED, CD PROJECT',
#         "publishers": 'CD PROJECT RED',
#         "inCart": false,
#         "selected": false,
#         "isHovered": false,
#         "isLiked": false,
#         "rating": 78,
#         id: 0,
#         cover: "https://res.cloudinary.com/gianlucajahn/image/upload/c_scale,q_100,w_500/v1658188604/cyberpunk_n6jitl.jpg",
#         footage: [
#             "https://res.cloudinary.com/gianlucajahn/image/upload/v1658188604/cyberpunk_n6jitl.jpg",
#             "https://res.cloudinary.com/gianlucajahn/image/upload/c_scale,q_100,w_1920/v1658235373/cyberpunk_1_s00vwf.jpg",
#             "https://res.cloudinary.com/gianlucajahn/image/upload/c_scale,q_100,w_1920/v1658235372/cyberpunk_2_mq46xm.jpg",
#             "https://res.cloudinary.com/gianlucajahn/image/upload/c_scale,q_100,w_1920/v1658235378/cyberpunk_3_fajdmi.jpg"
#         ]
#     }
