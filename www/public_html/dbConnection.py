#!C:\dev\python\3.12.4\_python\python

import mariadb;

def executeQuery(query):
    try:
        conn = mariadb.connect(
            user = "root",
            password = "",
            host = "127.0.0.1",
            port = 3306,
            database = "sakila"
        )
    except mariadb.Error as e:
        print("Error connecting to mariaDB")
        
    cur = conn.cursor()

    cur.execute(query)
    
    return cur
    
def printTable(cur):
    print('''
            <table>
            <tr>
                <td>
                    ID
                </td>
                <td>
                    First Name
                </td>
                <td>
                    Last Name
                </td>
            </tr>

    ''');

    for actor_id, first_name, last_name, last_update in cur:
        print(f"<tr><td>{actor_id}</td><td>{first_name}</td><td>{last_name}</td></tr>")
        
    print('</table>');



print('''
    <html>
        <head>
            <style>
				table {
					border: 2px solid black;
					padding: 5px;
					margin: 5px;
				}
				td {	
					border: 2px solid black;
					text-align: center;
				}
			</style>
        </head>
        <body>
''')

cur = executeQuery("SELECT * FROM actor;")

printTable(cur)
    
print('''
    </body>
</html>
''');

