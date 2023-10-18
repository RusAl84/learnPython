import pymorphy2

morph = pymorphy2.MorphAnalyzer()
word = morph.parse("Синхрофазатроны")[0]
print(word)
