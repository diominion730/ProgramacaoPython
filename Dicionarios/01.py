#Nomes = ['Pedro', 'Arthur', 'Paulo']
#print(Nomes[2])
#Nomes.append('Clara')
#Nomes.pop(1)
#print(Nomes)

print("-----------PRINCIPAIS METODOS------------")

Pessoa = {'Nome':'Vincius', 'Idade': 18, 'Ocupaçao': 'Estudante'}

print(Pessoa.get('Nome'))
print(Pessoa['Idade'])
print(Pessoa.keys()) #Todas as chaves
print(Pessoa.values()) #Todos os valores
print(Pessoa.items) #Todos os pares
print(list(Pessoa.keys())[0]) #Chave especifica
print(list(Pessoa.values())[1]) #Valor especifico
print(list(Pessoa.items())[0]) #Par especifico

#Pessoa.pop('Nome') #Apaga um par pela Chave
Pessoa.update({'Apelido': 'Vini'}) #Adiciona
Pessoa.update({'Nome': 'Vinicius Gomes'})
#Pessoa.popitem() #Remove o ultimo par chave-valor do dic
print(Pessoa)

