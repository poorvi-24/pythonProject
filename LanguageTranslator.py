from googletrans import Translator, LANGUAGES
SampleText=input("enter text :")
lang=input("enter the language:")
t=Translator().translate(SampleText,lang)
print(t.text)