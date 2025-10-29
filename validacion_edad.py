def discoteca(edad):
    if edad <18:
        return "Acceso denegado , el usuario es menor de edad"
    else:
        return "Acceso otorgado"
fila = {"Andres":18,"Felipe":17,"Sara":16,"Samuel":20,"Daniel":19}
for persona in fila:
    acceso= discoteca(fila[persona])
    print(f"{acceso}, ({persona})")
