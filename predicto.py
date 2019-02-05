from fbprophet import Prophet
import pandas as pd

def make_dataframe(data, columns=['datetime', 'items']):
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