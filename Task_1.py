# -- Q1 --

def my_func(x1, x2, x3):
    try:
        if not (isinstance(x1, float) and isinstance(x2, float) and isinstance(x3, float)):
            print("Error: parameters should be float")
            return None
        else:
            result = ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
            return float(result)
    except ZeroDivisionError:
        print("Not a number - denominator equals zero")

# -- Q2 --

def reword(word):
    return word[::-1].lower()

def countword():
    with open(r"C:\עידו\אוניברסיטת אריאל\שנה ג\סמסטר ב\כרייה וניתוח נתונים מתקדם בפייתון\מטלה 1\text.txt") as f:
        lines = f.readlines()
        word = lines[0].rstrip()
        counter = 1
        for i, line in enumerate(lines):
            if i == 0:
                continue
            line = line.rstrip()
            for w in line.split():
                if reword(w) == word:
                    counter += 1
        return counter
print(countword())
