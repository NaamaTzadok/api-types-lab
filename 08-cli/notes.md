## CLI API Lab Notes

### get-post 1 Output:
```text
Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
```

### list-users Output:
```text
1: Leanne Graham (Sincere@april.biz)
2: Ervin Howell (Shanna@melissa.tv)
3: Clementine Bauch (Nathan@yesenia.net)
4: Patricia Lebsack (Julianne.OConner@kory.org)
5: Chelsey Dietrich (Lucio_Hettinger@annie.ca)
6: Mrs. Dennis Schulist (Karley_Dach@jasper.info)
7: Kurtis Weissnat (Telly.Hoeger@billy.biz)
8: Nicholas Runolfsdottir V (Sherwood@rosamond.me)
9: Glenna Reichert (Chaim_McDermott@dana.io)
10: Clementina DuBuque (Rey.Padberg@karina.biz)
```

### Question:
מדוע CLI אינו נחשב סוג API אלא ממשק, ומה קורה ברשת מאחורי הקלעים כאשר מריצים פקודה כמו gh repo list?

### Answer:
API הוא הממשק של אפליקציה שהלקוח מדבר איתה דרך האינטרנט, ו-CLI הוא הממשק ידידותי למשתמש דרך שורת הפקודה לא בהכרח עבור תקשורת ברשת.
לדוגמא כאשר מריצים את הפקודה gh repo list הCLI של גיטהאב שמותקן לוקאלית מפענח את הפקודה ומתרגם אותה לבקשת http מתאימה שנשלחת לשרתים של גיטהאב (api רגיל) ומחזיר את התוצאה. 