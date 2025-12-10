class Soda:
    def __init__(self, flavor):
        self.flavor = flavor
    
    def sprinkle_water(self):
        if self.flavor:
            return f"Sprinkling water on {self.flavor} soda."
        else:
            return "No flavor specified for the soda."

# Example usage:
soda = Soda("Cola")
print(soda.sprinkle_water())

soda_no_flavor = Soda("")
print(soda_no_flavor.sprinkle_water())
