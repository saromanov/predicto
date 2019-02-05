from fbprophet import Prophet
import pandas as pd
import sqlalchemy
import psycopg2

class Predicto:
    """ definition of the Predicto class
    """
    def __init__(self, datetimeCol, database=None, user=None, host=None, password=None):
        self._datetimeCol = datetimeCol
        connect = psycopg2.connect(database=database, user=user, host=host, password=password)
        self._cursor = connect.cursor() 
    
    def __repr__(self):
        return type(self).__name__
    
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