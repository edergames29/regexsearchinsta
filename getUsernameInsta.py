import re
instajson = open('www.instagram.com.har','r').read()

compilado = re.compile(r'\"username\\":\\"(.+?)"(,|}}}}]}}},)?')
lista = re.findall(compilado,instajson)

print(lista)
print(len(lista))
