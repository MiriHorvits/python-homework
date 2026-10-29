import os

def file_manager():
    while True:
        print("\n--- מערכת לניהול קבצים ותיקיות ---")
        print("1. יצירת תיקיה חדשה")
        print("2. מחיקת תיקיה קיימת (אם היא ריקה)")
        print("3. יצירת קובץ חדש")
        print("4. כתיבה או הוספת תוכן לקובץ קיים")
        print("5. מחיקת קובץ")
        print("6. רשימת כל הקבצים והתיקיות בתיקיה")
        print("7. הצגת נתיב מלא של התיקיה הנוכחית")
        print("8. יציאה")
        
        choice = input("בחר אפשרות (1-8): ")
        
        if choice == '1':
            path = input("הכנס את נתיב התיקיה ליצירה: ")
            try:
                os.mkdir(path)
                print("התיקיה נוצרה בהצלחה.")
            except Exception as e:
                print(f"שגיאה ביצירת התיקיה: {e}")
                
        elif choice == '2':
            path = input("הכנס את נתיב התיקיה למחיקה: ")
            try:
                os.rmdir(path)
                print("התיקיה נמחקה בהצלחה.")
            except Exception as e:
                print(f"שגיאה במחיקת התיקיה (ודא שהיא ריקה): {e}")
                
        elif choice == '3':
            filename = input("הכנס את שם הקובץ (או הנתיב) ליצירה: ")
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    print("הקובץ נוצר בהצלחה.")
            except Exception as e:
                print(f"שגיאה ביצירת הקובץ: {e}")
                
        elif choice == '4':
            filename = input("הכנס את שם הקובץ לכתיבה: ")
            mode = input("בחר מצב - כתיבה מחדש (w) או הוספת תוכן לסוף (a): ")
            if mode not in ['w', 'a']:
                print("בחירה שגויה.")
                continue
            content = input("הכנס את התוכן לכתיבה: ")
            try:
                with open(filename, mode, encoding='utf-8') as f:
                    f.write(content + "\n")
                print("התוכן נשמר בהצלחה.")
            except Exception as e:
                print(f"שגיאה בכתיבה לקובץ: {e}")
                
        elif choice == '5':
            filename = input("הכנס את שם הקובץ למחיקה: ")
            try:
                os.remove(filename)
                print("הקובץ נמחק בהצלחה.")
            except Exception as e:
                print(f"שגיאה במחיקת הקובץ: {e}")
                
        elif choice == '6':
            path = input("הכנס את נתיב התיקיה (השאר ריק עבור תיקיה נוכחית): ")
            if not path:
                path = "."
            try:
                items = os.listdir(path)
                print("תוכן התיקיה:")
                for item in items:
                    print("-", item)
            except Exception as e:
                print(f"שגיאה בהצגת תוכן התיקיה: {e}")
                
        elif choice == '7':
            print(f"הנתיב המלא של התיקיה הנוכחית: {os.getcwd()}")
            
        elif choice == '8':
            print("להתראות!")
            break
        else:
            print("אפשרות שגוי, אנא בחר מספר בין 1 ל-8.")

if __name__ == "__main__":
    file_manager()
