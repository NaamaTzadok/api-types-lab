## GraphQL API Lab Notes

### Client Output:
```text
Titles only -> {'data': {'books': [{'title': 'Clean Code'}, {'title': 'The Pragmatic Programmer'}]}}
Full book -> {'data': {'book': {'id': 1, 'title': 'Clean Code', 'author': 'Robert Martin'}}}
Mutation -> {'data': {'addBook': {'id': 3, 'title': 'Domain-Driven Design'}}}
```

### Question:
איזו בעיה ב-```REST``` פותר ```GraphQL```, ומדוע דווקא בגלל הפתרון הזה קאשינג הופך למורכב יותר?

### Answer:
ב```REST``` יש לכל אנדפוינט נתיב מוגדר ותבנית קבועה של נתונים שמוחזרים באותה אנדפוינט. ב```GraphQL``` לעומת זאת, יש אנדפוינט אחת שבה הקליינט מגדיר איזה נתונים הוא צריך ומקבל רק אותם. כך הלקוח לא מקבל מידע מיותר, ומקבל בדיוק מה שהוא צריך. החסרון הוא שב-```REST``` יכלנו לבצע קאשינג על סמך ה- ```URL``` המדויק, ופה זה נעשה יותר מורכב כי הכל נמצא באנדפוינט אחת. ולכן צריך להשתמש בספריות צד לקוח ששומרות את הנתונים לפי ה-```id```, או על ידי שאילתות שמיוצאות מראש בזמן ה```build```. 