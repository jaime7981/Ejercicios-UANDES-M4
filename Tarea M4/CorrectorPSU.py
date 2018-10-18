PSU = {"PAUTA" : ["a","b","c","d","e","a","b","c","d","e","a","b","c","d","e","a","b","c","d","e","e","e","e"]}
resultados = {}
alumnos = []
n = int(input())
for a in range(n):
    alumno = input().split(",")
    PSU[alumno[0]] = alumno[1:]
    alumnos.append(alumno[0])
for a in range(len(alumnos)):
    correctas = 0
    for b in range(23):
        if PSU["PAUTA"][b] == PSU[alumnos[a]][b]:
            correctas += 1
        else:
            pass
    resultados[alumnos[a]] = correctas
for a in range(len(alumnos)):
    if 15 < int(resultados[alumnos[a]]):
        print(alumnos[a], resultados[alumnos[a]])
