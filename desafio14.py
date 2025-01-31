nomes = ["Joao","Maria","Barbara","Pedro","Ana","Vinicius","Barbara","Joao","Pedro","Rafael","Isabella", "Matheus","Laura","Guilherme","Sofia","Vinicius","Amanda","Leonardo","Gabriela"]

n = []
for nome in nomes:
    if nome not in n:
        n.append(nome)

print("Apresente a lista antiga:", nomes)
print("Apresente a nova lista:", n)