import os

# Lancer un programme externe
test = os.system('ls')


# Lancer un programme externe et récupérer le résultat
result = os.popen('ls').read()
print(result)


# Gestion des droits et permissions
# os.chmod('test.txt', 0o777)
