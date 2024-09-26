import pathlib


# Dossier utilisateur
home = pathlib.Path.home()
print(home)


# Dossier courant
current = pathlib.Path.cwd()
print(current)


# Chemin spécifique
specific = pathlib.Path('/home/gabrieltrouve/Pro/mentorats/m_27092024/')
print(specific.exists())

# Concaténation de chemins (utilisation des répertoires parents)
concat = specific / 'test' / 'test'
concat.mkdir(parents=True, exist_ok=True)
