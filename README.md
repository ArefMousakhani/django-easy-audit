#### This Project Retrieved From [django-easy-audit](https://github.com/soynatan/django-easy-audit )

# django-easy-audit-mongodb

Yet another Django audit log app, hopefully the easiest one.

This app allows you to keep track of every action taken by your users.

## Quickstart

1. First Install `pymongo` by running `pip install pymongo`.

2. install `easyaudit_mongodb`:

    ``` 
    wget https://github.com/ArefMousakhani/django-easy-audit/blob/master/easyaudit_mongodb-0.1.tar.gz
    ```

    then 
    
    ```
    pip install ./easyaudit_mongodb-0.1.tar.gz
    ```
2. Add `easyaudit_mongodb` to your `INSTALLED_APPS` like this:

    ```python
    INSTALLED_APPS = [
        ...
        'easyaudit_mongodb',
    ]
    ```

3. Add Easy Audit's middleware to your `MIDDLEWARE` (or `MIDDLEWARE_CLASSES`) setting like this:

    ```python
    MIDDLEWARE = (
        ...
        'easyaudit_mongodb.middleware.easyaudit.EasyAuditMiddleware',
    )
    ```

4. Add Mongodb Config to your django `settings.py`:

    ```python
    MONGODB_ADDRESS = 'mongodb://localhost:27017/'
    MONGODB_NAME = 'EasyAudit'
    MONGODB_CRUD_COLLECTION_NAME = 'CRUDEvent'
    MONGODB_LOGIN_COLLECTION_NAME = 'LoginEvent'
    MONGODB_REQUEST_COLLECTION_NAME = 'RequestEvent'
    ```

## Contact

[aref.mouskhani@gmail.com](mailto:aref.mousakhani@gmail.com)
