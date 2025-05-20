
taches = []


def ajouter(titre):
    taches.append({"titre": titre, "faite": False})
    print(f"Tâche ajoutée : {titre}")


def lister():
    if not taches:
        print("Aucune tâche.")
        return
    for i, t in enumerate(taches, 1):
        status = "✅" if t["faite"] else "❌"
        print(f"{i}. [{status}] {t['titre']}")


def marquer_faite(num):
    if num < 1 or num > len(taches):
        print("Numéro invalide.")
        return
    taches[num - 1]["faite"] = True
    print(f"Tâche {num} marquée comme faite.")


def supprimer(num):
    if num < 1 or num > len(taches):
        print("Numéro invalide.")
        return
    supprimée = taches.pop(num - 1)
    print(f"Tâche supprimée : {supprimée['titre']}")
    
    
def execut():
    ajouter("Faire les courses")
    ajouter("Réviser Python")
    lister()
    marquer_faite(1)
    lister()
    supprimer(2)
    lister()
    
execut()