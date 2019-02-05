from fbprophet import Prophet
import pandas as pd
import sqlalchemy
import psycopg2

class Predicto:
    """ definition of the Predicto class
    """
    def __init__(self, datetimeCol, database=None, user=None, host=None, password=None):
        self._datetimeCol = datetimeCol
        self._connect = psycopg2.connect(database=database, user=user, password=password)
        self._cursor = self._connect.cursor() 
    
    def __repr__(self):
        return type(self).__name__
    
    def query(self, expr):
        """ apply query to postgesql
        
        :param: expr: string with query like SELECT * FROM base;
        """
        self._cursor.execute(expr)
    
    def fit(self, X, labels):
        """ fitting of data

        :param X: data for base for making predictions
        :labels: list of the labels for making dataframe
        """
        labels = [self._datetimeCol]
        labels.extend(labels)
        df = self._make_dataframe(X, colums=labels)
        return self._predict(df)
    
    def _make_dataframe(data, columns=['datetime', 'items']):
        """returns pandas dataframe
        """
        return pd.DataFrame(data, columns=columns)
    
    def _predict(data):
        """ predicting of the future data points
        based on exist data
        """
        p = Prophet()
        p.fit(data)
        future = p.make_future_dataframe(periods=366)
        return p.predict(future)
    
    def close(self):
        """ close provides closing connection to db
        """
        self._connect.close()