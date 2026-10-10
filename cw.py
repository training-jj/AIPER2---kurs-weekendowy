
dni_tygodnia = {
    1: "Poniedziałek",
    2: "Wtorek",
    3: "Środa",
    4: "Czwartek",
    5: "Piątek",
    6: "Sobota",
    7: "Niedziela"
}

numer = int(input("Podaj numer dnia tygodnia (1-7): "))

if numer in dni_tygodnia:
    print("Dzień tygodnia:", dni_tygodnia[numer])
else:
    print("Nieprawidłowy numer dnia!")
