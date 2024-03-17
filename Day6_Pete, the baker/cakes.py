def cakes(recipe, available):
    potential_cakes = []

    for bahan, jumlah in recipe.items():
        if bahan in available:
            potential_cakes.append(available[bahan] // jumlah)
        else:
            return 0

    return min(potential_cakes)

print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))  # Output: 2
print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000}))  # Output: 0
