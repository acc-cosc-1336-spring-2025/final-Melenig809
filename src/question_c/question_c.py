def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    for i in range(len(dna_string1) - len(dna_string2) + 1):
        if dna_string1[i:i+len(dna_string2)] == dna_string2:
            positions.append(i + 1)
    
    return tuple(positions)

dna_string1 = "GATATATGCATATACTT"
dna_string2 = "ATAT"

result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)

print("Positions:", *result)
