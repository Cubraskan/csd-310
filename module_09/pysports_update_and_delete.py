import mysql.connector
from mysql.connector import errorcode

config = {
    "user":"pysports_user",
    "password":"MySQL8IsGreat!",
    "host":"127.0.0.1",
    "database":"pysports",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

cursor.execute("INSERT INTO player (player_id, first_name, last_name, team_id) VALUES(21, 'Smeagol', 'Shire Folk', 1);")
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player RIGHT OUTER JOIN team ON player.team_id = team.team_id;")
players = cursor.fetchall()
player_list = players.sort()

print ("-- DISPLAYING PLAYERS AFTER INSERT --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}\n".format(player[3]))

cursor.execute("UPDATE player SET team_id = 2, FIRST_NAME = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';")
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player RIGHT OUTER JOIN team ON player.team_id = team.team_id;")
players = cursor.fetchall()
player_list = players.sort()

print ("-- DISPLAYING PLAYERS AFTER UPDATE --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}\n".format(player[3]))

cursor.execute("DELETE FROM player where first_name = 'Gollum';")
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player RIGHT OUTER JOIN team ON player.team_id = team.team_id;")
players = cursor.fetchall()
player_list = players.sort()

print ("-- DISPLAYING PLAYERS AFTER DELETE --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}\n".format(player[3]))

print("\n\n Press any key to continue...")
