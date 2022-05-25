def find():
    text = "X-DSPAM-Confidence:0.8475"
    a =float(text[19:25])
    return a

x=find()
print(x)