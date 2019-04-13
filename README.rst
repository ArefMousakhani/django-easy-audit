#### This Project Retrieved From [django-easy-audit](https://github.com/soynatan/django-easy-audit )

# django-easy-audit-mongodb

Yet another Django audit log app, hopefully the easiest one.

This app allows you to keep track of every action taken by your users.

## Quickstart

1. First Install `pymongo` by running `pip install pymongo`.


2. Add 'easyaudit' to your `INSTALLED_APPS` like this:

    ```python
    INSTALLED_APPS = [
        ...
        'easyaudit-mongodb',
    ]
    ```

3. Add Easy Audit's middleware to your `MIDDLEWARE` (or `MIDDLEWARE_CLASSES`) setting like this:

    ```python
    MIDDLEWARE = (
        ...
        'easyaudit-mongodb.middleware.easyaudit.EasyAuditMiddleware',
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
