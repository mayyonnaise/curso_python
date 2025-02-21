produtos = ("Batata Frita", 6.79, "Biscoito", 4.45, "Doce de Leite com Chocolate", 9.39, "Granola de Quinoa com Castanhas", 14.45, "Café Torrado e Moído", 20.25, "Pé de Moleque 400g", 24.9, "Cereal em Barra Damasco e Ameixa", 4.99, "Farelo de Aveia", 4.49, "Alimento Vitaminado", 5.69, "Ração para Gatos 3Kg", 40.75, "Feijão 1Kg", 3.49, "Kit de Shampoo", 16.9, "Fondue Suiço de Queijo", 44.9, "Fraudas 60un", 75.9, "Vinho Argentino", 62.9, "Leite Condensado", 4.35, "Água Mineral", 2.49, "Isotônico", 3.95, "Detergente", 1.39, "Ervilha", 1.89, "Milho Verde", 1.69, "Refrigerante Lata", 2.39, "Fubá de Milho", 2.35, "Sabonete", 2.99, "Creme Dental", 2.79, "Arroz 1Kg", 3.49, "Salgadinho", 3.19)

print("╔" + 49 * "═" + "╗")
print("║" + "Lista de Compras".center(49) + "║")
print("╠" + 49 * "═" + "╣")

for i in range(0, len(produtos), 2):
 print(f"║ {produtos[i]}".ljust(40, ".") + "R$" + f"{produtos[i+1]:.2f}".rjust(7) + " ║")

print("╚" + 49 * "═" + "╝")