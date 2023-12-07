import pymorphy2

morph = pymorphy2.MorphAnalyzer()
word = morph.parse("Машины")[0]
print(word.normal_form)
