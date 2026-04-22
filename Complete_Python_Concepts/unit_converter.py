print("=== UNIT CONVERTER ===")

print("\nChoose conversion:")
print("1. Kilograms to Grams")
print("2. Kilometers to Meters")
print("3. Celsius to Fahrenheit")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    kg = float(input("Enter kg: "))
    print("Grams:", kg * 1000)

elif choice == "2":
    km = float(input("Enter km: "))
    print("Meters:", km * 1000)

elif choice == "3":
    c = float(input("Enter Celsius: "))
    f = (c * 9/5) + 32
    print("Fahrenheit:", f)

else:
    print("Invalid choice")