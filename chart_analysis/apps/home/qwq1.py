import textract
text = textract.process(r"q.doc")
text = text.decode()
print(text)

with open('111.txt','w',encoding='utf-8') as f:
        f.write(str(text))
