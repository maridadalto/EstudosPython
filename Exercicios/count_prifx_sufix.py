def countPrefixSuffixPairs(strings):
    # Passo 1: Inicializar a contagem
    count = 0
    
    # Passo 2: Iterar sobre os elementos da lista
    for string in strings:
        n = len(string)
        # Passo 3: Iterar sobre os possíveis prefixos e sufixos
        for i in range(n):
            for j in range(i+1, n):
                prefix = string[:i+1]  # Prefixo vai do início até o elemento atual
                suffix = string[j:]    # Sufixo vai do elemento atual até o final
                
                # Passo 4: Comparar prefixo com sufixo
                if prefix == suffix:
                    # Passo 5: Incrementar a contagem
                    count += 1
    
    # Passo 6: Retornar o resultado
    return count
