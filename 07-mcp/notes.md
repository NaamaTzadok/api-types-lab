## MCP API Lab Notes

### calculate_streak_bonus Output with days=30:
```text
90
```

### get_role_categories Output with role="devops":
```text
["Linux", "Docker", "Kubernetes", "CI/CD", "Cloud"]
```

### Question:
מי הצרכן המיועד של MCP server, ומדוע ניסוח ה-docstring של tool הוא קריטי לתפקוד הנכון, בניגוד לתיעוד רגיל ב-REST?

### Answer:
הצרכן הוא מודל שפה כלשהו, ניסוח ה-docstring עוזר למודל להבין את השימוש של הפונקציה, מתי להשתמש בכלי ואיך. ולכן חשוב לנסח אותו בצורה מדויקת כדי שהמודל ידע לעשות בו שימוש נכון. וזה בניגוד ל-REST שהלקוח שלו הוא אפליקצית דפדפן קבועה שבזמן שהיא נכתבת נקבע השימוש המדויק בAPI על ידי המתכנת.