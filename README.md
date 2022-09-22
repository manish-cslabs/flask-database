# FLASK REST API using SQL

- **Reference:** [Python REST API Tutorial - Building a Flask REST API](https://www.youtube.com/watch?v=GMppyAPbLYk)


```python
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy #ORM
```

- **Api:** for restful api creation
- **Resource:** used while creating class for RESTful functions
- **reqparse:** ReqParse is used to parse request parameters sent with requests
- **abort:** is used to abort the request when excepion is encountered
- **fields:** used to define variable type in serializable object
- **marshal_with:** used toserialize and unserialize objects
- **SQLAlchemy:** object relational mapping library