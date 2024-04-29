def isAnagram(s: str, t: str) -> bool:
    # Passo 1: Ordenar as strings
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    
    # Passo 2: Comparar as strings ordenadas
    return sorted_s == sorted_t
