import psycopg2
from .config import config

class UnauthorisedAccessError(Exception):
    pass

class stockdb(object):
    __authenticated = False
    __cur = None
    __conn = None

    def __init__(self, userid=None, password=None):
        # read connection parameters
        params = config()
        # update connection parameters as per user request
        if userid is not None:
            params['user'] = userid
        if password is not None:
            params['password'] = password
        self.__connect(params)
        if self.__conn is not None and userid is not None and password is not None:    
            self.__authenticated = True

    #def __init__(self):
    #    # read connection parameters
    #    params = config()
    #    self.__connect(params)
        
    def __connect(self, params):
        try:
            # connect to the PostgreSQL server
            # print('Connecting to the PostgreSQL database...')
            self.__conn = psycopg2.connect(**params)
            
            # create a cursor
            self.__cur = self.__conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def stock_price(self,ticker,date,time_window):
        if time_window>90 and self.__authenticated==False:
            raise UnauthorisedAccessError("Cannot access more than 90 days of prices without authentication")
            return
        
        query = "SELECT day,price from imported_closes WHERE day<=TO_DATE('"+date+"', '%Y %M %D') AND day>(TO_DATE('"+date+"', '%Y %M %D')::timestamp - '"+str(time_window)+" days'::interval) AND ticker='"+ticker+"'"
        
        try:
            self.__cur.execute(query)
            response = self.__cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return response

