from fbprophet import Prophet

def predict(data):
    """ predicting of the future data points
    based on exist data
    """
    p = Prophet()
    p.fit(data)
    future = p.make_future_dataframe(periods=366)
    return p.predict(future)