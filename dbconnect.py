import sqlite3

import config


class DatabaseConnection:
    def __init__(self, databaseName):
        self.databaseName = databaseName
        self.connected = False
        self.tables = []

    def connect(self):
        try:
            conn = sqlite3.connect(f'{self.databaseName}')
            cursor = conn.cursor()
            print("Database created and successfully connected.")
            self.connected = True
            cursor.close()

        except sqlite3.Error as error:
            print(f"Could not connect to the database {self.databaseName}")
        finally:
            if conn:
                conn.close()
                print(f"The connection to {self.databaseName} has now been closed")

    def SetupTables(self):
        try:
            # [------ Creating Teams Table -----]
            conn = sqlite3.connect(f'{self.databaseName}')
            cursor = conn.cursor()
            print('Successful connection:')
            cursor.execute(config.createTeams)
            conn.commit()
            print("Teams Table Created")

            # [------- Creating Sightings Table ------ ]
            conn = sqlite3.connect(f'{self.databaseName}')
            cursor = conn.cursor()
            print('Successful connection:')
            cursor.execute(config.createSightings)
            conn.commit()
            print("Sightings Table Created")

            cursor.close()

        except sqlite3.Error as error:
            print(error)
            print("Could not create the tables")
        finally:
            if conn:
                conn.close()
                print('Connection is now closed')

    def addTeam(self, Name, local_id, global_id, dateJoined):
        try:
            conn = sqlite3.connect(self.databaseName)
            cursor = conn.cursor()
            addaTeam = (f'''INSERT INTO Teams (TeamName, uuid_local, uuid_global, dateJoined) VALUES ("{Name}","{local_id}","{global_id}","{dateJoined}");''')
            cursor.execute(addaTeam)
            conn.commit()
            print(f"Record Created: {cursor.rowcount}")
            cursor.close()
        except sqlite3.Error as e:
            print(f"Failed: {e}")
        finally:
            if conn:
                conn.close()
                print("Then Connection is now closed")

    def addSighting(self, team, local_id, global_id, lat, long, timeSighted, dmslat, dmslong):
        try:
            conn = sqlite3.connect(self.databaseName)
            cursor = conn.cursor()
            addaSighting = (f'''INSERT INTO Sightings (Team, 
                                                       LocalID, 
                                                       GlobalID, 
                                                       Latitude, 
                                                       Longitude, 
                                                       TimeSighted, 
                                                       DMS_lat, 
                                                       DMS_long) 
                                                       VALUES 
                                                       ("{team}",
                                                       "{local_id}",
                                                       "{global_id}",
                                                       "{lat}", 
                                                       "{long}", 
                                                       "{timeSighted}", 
                                                       "{dmslat}",
                                                       "{dmslong}")''')
            cursor.execute(addaSighting)
            conn.commit()
            print(f"Record Created for Sighting: {cursor.rowcount}")
            cursor.close()
        except sqlite3.Error as e:
            print(f"Failed: {e}")
        finally:
            if conn:
                conn.close()
                print("The connection has been closed.")