a = int(input("First day of jogging in km "))
b = int(input("Your aim in jogging in km"))
days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        days += 1
        result_km = result_km + a
print(f"You are going to success on %.d th day" % days)