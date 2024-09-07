from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def ottieniNodi(year):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select state1no as s1no, state2no as s2no
                    from contiguity c 
                    where c.year<=%s
                             """
        cursor.execute(query, (year, ))
        for row in cursor:
            if row["s1no"] not in result:
                result. append(row["s1no"])
            if row["s1no"] not in result:
                result. append(row["s1no"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def ottieniArchi(year):
            conn = DBConnect.get_connection()
            result = []
            cursor = conn.cursor(dictionary=True)
            query = """ select state1no as s1no, state2no as s2no
                        from contiguity c 
                        where c.year<=%s and c.conttype=1
                    """
            cursor.execute(query, (year,))
            for row in cursor:
                result.append((row["s1no"],row["s2no"]))
            cursor.close()
            conn.close()
            return result

    @staticmethod
    def nomi():
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = """ select Ccode as no, StateNme na
                           from country c 
                           
                       """
        cursor.execute(query, () )
        for row in cursor:
            result[row["no"]]= row["na"]
        cursor.close()
        conn.close()
        return result



