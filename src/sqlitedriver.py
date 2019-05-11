import sqlite3, threading

class sqliteclass(object):
    def __init__(self, fileName):
        self.fileName = fileName
        self.createTable()

    def createTable(self):
        error = None
        result = True
        with sqlite3.connect(self.fileName) as conn:
            c = conn.cursor()
            # Create table
            try:
                c.execute('''CREATE TABLE IF NOT EXISTS urls (sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, shorturl text, longurl text)''')
                conn.commit()
            except Exception as e:
                error = str(e)
                result = False
            finally:
                c.close()
        return result, error

    def insertData(self, shorturl, longurl):
        error = None
        result = True
        with sqlite3.connect(self.fileName) as conn:
            c = conn.cursor()
            # Insert a row of data
            sql = '''INSERT INTO urls(shorturl, longurl)
                         VALUES(?,?) '''
            parms = (shorturl, longurl)
            try:
                c.execute(sql, parms)
                conn.commit()
            except Exception as e:
                error = str(e)
                result = False
            finally:
                c.close()
        return result, error
        
    def readShortUrl(self, longurl):
        error = None
        result = None
        with sqlite3.connect(self.fileName) as conn:
            c = conn.cursor()
            sql = '''SELECT shorturl FROM urls where longurl = ?'''
            try:
                c.execute(sql, [longurl])
                row = c.fetchone()
                if row is not None:
                    result = row[0]
            except Exception as e:
                error = str(e)
            finally:
                c.close()
        return result, error

    def readLongUrl(self, shorturl):
        error = None
        result = None
        with sqlite3.connect(self.fileName) as conn:
            c = conn.cursor()
            sql = '''SELECT longurl FROM urls where shorturl = ?'''
            try:
                c.execute(sql, [shorturl])
                row = c.fetchone()
                if row is not None:
                    result = row[0]
            except Exception as e:
                error = str(e)
            finally:
                c.close()
        return result, error

    def deleteShortUrl(self, longurl):
        error = None
        with sqlite3.connect(self.fileName) as conn:
            c = conn.cursor()
            sql = '''DELETE from urls where longurl = ?'''
            try:
                c.execute(sql, [longurl])
                conn.commit()
                result = c.rowcount
            except Exception as e:
                error = str(e)
                result = 0
            finally:
                c.close()
        return result, error