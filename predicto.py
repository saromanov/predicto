from fbprophet import Prophet
import pandas as pd


class Predicto:
    """ definition of the Predicto class
    """
    def __init__(self, datetimeCol):
        self._datetimeCol = datetimeCol
    
    def fit(self, X, labels):
        """ fitting of data
        """
        labels = [self._datetimeCol]
        labels.extend(labels)
        df = self._make_dataframe(X, colums=labels)
    
    def _make_dataframe(data, columns=['datetime', 'items']):
        """returns pandas dataframe
        """
        return pd.DataFrame(data, columns=columns)


def predict(data):
    """ predicting of the future data points
    based on exist data
    """
    p = Prophet()
    p.fit(data)
    future = p.make_future_dataframe(periods=366)
    return p.predict(future)