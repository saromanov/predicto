# predicto

Forecasting of the data from Postgresql

### Why?
For example, you have a users on your db and you need to forecast how much users will join during in the next week

### Install

### Example
```python
from predicto import Predicto

# Connect to postgesql
pred = Predicto('created', database='predicto', host='localhost', port=5432, user='predicto', password='predicto')

# aggregation data by the date
# it'll be in format (datetime, number_of_items)
result = pred.aggregate_by_date()

# prediction based on data
print(pred.fit(result))
```