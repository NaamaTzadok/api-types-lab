## Rest API Lab Notes

### Client Output:
```text
GET /books -> [{'id': 1, 'title': "Harry Potter and the Philosopher's Stone", 'author': 'J.K. Rowling'}, {'id': 2, 'title': 'The Hobbit', 'author': 'J.R.R. Tolkien'}]
POST /books -> 201 {'id': 3, 'title': 'The Lord of the Rings: The Fellowship of the Ring', 'author': 'J.R.R. Tolkien'}
GET /books/3 -> {'id': 3, 'title': 'The Lord of the Rings: The Fellowship of the Ring', 'author': 'J.R.R. Tolkien'}
PUT /books/3 -> {'id': 3, 'title': 'The Lord of the Rings: The Two Towers', 'author': 'J.R.R. Tolkien'}
DELETE /books/3 -> status 204
```

### Question:
מדוע ```REST``` מתואר כ-```stateless```, ומה היתרון של זה ביכולת לבצע ```scaling``` לשרת על פני מספר מכונות?

### Answer:
הארכיטקטורה של ```REST``` בנויה בצורה כזו שהשרת לא שומר מידע בזכרון על המשתמש. כל בקשה מהלקוח היא נפרדת ובלתי תלויה באחרות. יש לזה יתרונות, אפשר לפצל את הבקשות על פני כמה שרתים נפרדים בלי לדאוג לתלות בינהם. ואם שרת אחד קורס אפשר להעביר את כל הבקשות לשרת אחר בלי לדאוג למידע מסויים. יש לזה גם חסרון שכל בקשה מעט יותר כבדה כיון שהיא מכילה את כל הנתונים והקונטקסט שהשרת צריך בשביל לטפל בה.