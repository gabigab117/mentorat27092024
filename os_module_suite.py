import os


# Chemin absolu (racine système)
print(os.path.abspath("os_module_suite.py"))

# Chemin relatif (emplacement par rapport à l'emplacement du répertoire courant)
print(os.path.relpath("os_module_suite.py"))

# Chemin du dossier parent
print(os.path.dirname("pastouche/fichier.txt"))

# Vérifier si un chemin est un fichier
print(os.path.isfile("os_module_suite.py"))

# Vérifier si un chemin est un dossier
print(os.path.isdir("os_module_suite.py"))

# Vérifier si un chemin existe
print(os.path.exists("os_module_suite.py"))

# Jointure de chemins
print(os.path.join("test", "test2", "fichier.txt"))

