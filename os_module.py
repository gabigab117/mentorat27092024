import os


# os permet de manipuler des fichiers et des dossiers avec des fonctions
# contrairement à pathlib qui permet de manipuler des fichiers et des dossiers avec des objets

# Type du système d'exploitation
print(os.name)

# Informations sur le système d'exploitation
print(os.uname())

# Répertoire courant
print(os.getcwd())

# Liste des fichiers et dossiers
print(os.listdir())

# Créer un dossier
if not os.path.exists('test'):
    os.mkdir('test')
else:
    print('Le dossier existe déjà')

# Renommer un dossier
os.rename('test', 'test2')

# Supprimer un dossier
os.rmdir('test2')

# Créer des répertoires imbriqués
os.makedirs('test/test/test', exist_ok=True)

# Supprimer des répertoires imbriqués
os.removedirs('test/test/test')

# Créer un fichier
f = open('test.txt', 'w')
f.write('Hello World')
f.close()

# Possibilité d'utitiliser os.open pour ouvrir un fichier

# Supprimer un fichier
os.remove('test.txt')

# Si je veux supprimer un dossier avec des fichiers il faut utiliser shutil
# import shutil
# shutil.rmtree('test')
