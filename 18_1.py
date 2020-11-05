def Check(figure, mass_mass):
    mass_level = [10 ** x for x in reversed(range(len(mass_mass)))]
    for i in range(len(mass_level)):
        if figure//mass_level[i] == len(mass_mass[i]):
            figure -= (figure // mass_level[i]) * mass_level[i]
            return True
        else:
            return False


print(Check(251, [[1, 1], [2, 2, 2, 2, 2], [3]]))