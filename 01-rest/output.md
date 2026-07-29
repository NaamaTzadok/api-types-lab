## Rest API Client Output:

```text
GET /books -> [{'id': 1, 'title': 'Clean Code', ...}, {'id': 2, ...}]
POST /books -> 201 {'id': 3, 'title': 'Refactoring', 'author': 'Martin Fowler'}
GET /books/3 -> {'id': 3, 'title': 'Refactoring', ...}
PUT /books/3 -> {'id': 3, 'title': 'Refactoring 2nd Ed', ...}
DELETE /books/3 -> status 204
```