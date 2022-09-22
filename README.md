# FLASK REST API using SQL

- **Reference:** [Python REST API Tutorial - Building a Flask REST API](https://www.youtube.com/watch?v=GMppyAPbLYk)


```python
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy #ORM
```

- **Api:** for restful API creation
- **Resource:** used while creating class for RESTful functions
- **reqparse:** ReqParse is used to parse request parameters sent with requests
- **abort:** is used to abort the request when exception is encountered
- **fields:** used to define a variable type in a serializable object
- **marshal_with:** used to serialize and unserialize objects
- **SQLAlchemy:** object-relational mapping library