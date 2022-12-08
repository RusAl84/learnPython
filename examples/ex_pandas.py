import pandas as pd

df = pd.read_excel("1.xlsx")
l = df.values.tolist()

print(df)
# print(l[0][0])
avr = 0
for item in l:
    avr += int(item[1])
avr /= len(l)
avr = int(avr)
print(avr)
l.append(["Среднее значение", str(avr), ""])
df = pd.DataFrame([l])
df.columns = ['col1', 'col2', 'col3', 'col4']
df.to_excel("2.xls")
df.to_json("2.json")
df.to_html("2.html")