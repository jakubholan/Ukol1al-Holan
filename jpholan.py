#1. Vytvořte pole, které bude mít 5 stringových hodnot.
pole = ["hory", "lesy", "jezero", "pole", "voda"]
#VYpíšeme počáteční pole
print("Počáteční pole:", pole)

#2. Přidejte pomocí metody append() jeden prvek. - "vítr"
pole.append("vítr")
print("Po přidání 'vítr':", pole)

#3. Odstraňte pomocí metody remove() druhý prvek z pole.
pole.remove(pole[1]
print("Po odstranění druhého prvku:", pole)

#4. Zaměňte 5 hodnotu z pole za: "slunce"
pole[4] = "slunce"
print("Po zaměnění 5. hodnoty na 'slunce':", pole)

#5. Přidejte 2 stringové hodnoty pole pomocí metody extend().
pole.extend(["déšť", "vítr"])
print("Po přidání dvou hodnot ('déšť', 'vítr') pomocí extend ():", pole

#6. Vypište základní vytvořené pole a potom každé pole, ve kterém uděláte změnu.
print("Základnípole:" ["hory", "lesy", "jezero", "pole", "voda"])
print("Pole po všech změnách:", pole)
