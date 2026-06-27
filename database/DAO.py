from database.DB_connect import DBConnect
from model.team import Team


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct year
from teams
where year >=1980
order by year desc"""

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])



        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getTeams(anno1):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.ID,t.year,t.teamCode,t.divID,t.div_ID,t.teamRank,t.name
from teams t, appearances a 
where t.ID =a.teamID
and a.`year`= %s """

        cursor.execute(query,(anno1,))

        for row in cursor:
            results.append(Team(**row))



        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getEdges(anno1):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.ID ,SUM(s.salary) as peso
        from teams t, salaries s , appearances a 
        where t.ID =a.teamID and t.ID =s.teamID
        and a.`year` = %s
        group by t.ID"""

        cursor.execute(query, (anno1,))

        for row in cursor:
            results.append((row["ID"],row["peso"]))

        cursor.close()
        conn.close()
        return results





