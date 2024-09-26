import pathlib
from idlelib.pathbrowser import PathBrowser

# Pathlib a une approche orientée objet pour manipuler les chemins de fichiers

# Créer un objet Path
path = pathlib.Path('pathlib_module.py')


# Vérifier si le chemin existe
print(path.exists())


# Vérifier si le chemin est un fichier
print(path.is_file())


# Vérifier si le chemin est un répertoire
print(path.is_dir())


# Obtenir le nom du fichier
print(path.name)


# Obtenir l'extension du fichier
print(path.suffix)


# Obtenir le chemin absolu
print(path.absolute())


# Obtenir le répertoire parent
print(path.parent)


# glob() permet de lister les fichiers dans un répertoire
for file in pathlib.Path('.').glob('*.py'):
    print(file)


# Tout lister dans un répertoire
for file in pathlib.Path('.').iterdir():
    print(file)


# Créer un répertoire
pathlib.Path('test').mkdir()


# Supprimer un répertoire
pathlib.Path('test').rmdir()

# Créer / Supprimer un fichier
path = pathlib.Path('test.txt')
path.touch()
path.write_text("Coucou")
path.read_text()
path.unlink()



