from fbprophet import Prophet
import pandas as pd
import psycopg2


class Predicto:
    """ definition of the Predicto class
    """

    def __init__(self, datetimeCol,
                 database=None,
                 user=None,
                 host=None,
                 port=None,
                 password=None):
        self._database = database
        self._datetimeCol = datetimeCol
        self._connect = psycopg2.connect(
            database=database,
            host=host,
            port=port,
            user=user,
            password=password)
        self._cursor = self._connect.cursor()

    def __repr__(self):
        return type(self).__name__

    def aggregate(self, expr):
        """ apply aggregation to postgesql. It should return two columns
        datetime and number of items

        :param: expr: string with query should aggregate timestamp with items
        """
        return self._aggregate(expr)

    def aggregate_by_date(self, timeframe='day'):
        """ its a helpful method for making aggregation by the date
        """
        query = "SELECT date_trunc('{0}', {1}), COUNT(1) FROM {2} GROUP BY 1".format(
            timeframe, self._datetimeCol, self._database)
        return self._aggregate(query)

    def _aggregate(self, expr):
        """ general method for aggregation from postgresql
        """
        self._cursor.execute(query)
        for res in self._cursor:
                yield res

    def fit(self, X):
        """ fitting of data

        :param X: data for base for making predictions
        """
        df = self._make_dataframe(X)
        return self._predict(df)

    def _make_dataframe(self, data):
        """returns pandas dataframe
        """
        result = list(
            map(lambda x: [x[0].isoformat(' ', 'hours'), x[1]], data))
        return pd.DataFrame(result, columns=['ds', 'y'])

    def _predict(self, data):
        """ predicting of the future data points
        based on exist data
        """
        p = Prophet()
        p.fit(data)
        future = p.make_future_dataframe(periods=10)
        return p.predict(future)

    def close(self):
        """ close provides closing connection to db
        """
        self._connect.close()
