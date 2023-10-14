# Parent class - TechDevice
class TechDevice:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print(f"{self.brand} {self.model} is turned on")

    def turn_off(self):
        print(f"{self.brand} {self.model} is turned off")

# Subclass - Smartphone, inherits from TechDevice
class Smartphone(TechDevice):
    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling number {number}")

    def send_text(self, number, message):
        print(f"{self.brand} {self.model} is sending a message to number {number}: {message}")

# Subclass - Tablet, inherits from TechDevice
class Tablet(TechDevice):
    def browse_web(self, url):
        print(f"{self.brand} {self.model} is browsing the website at URL: {url}")

# Subclass - Laptop, inherits from TechDevice
class Laptop(TechDevice):
    def run_application(self, app_name):
        print(f"{self.brand} {self.model} is running the application: {app_name}")

if __name__ == "__main__":
    smartphone = Smartphone("Samsung", "Galaxy S20")
    smartphone.turn_on()
    smartphone.make_call("123-456-789")
    smartphone.send_text("123-456-789", "Hello, how are you?")
    smartphone.turn_off()

    tablet = Tablet("Apple", "iPad Pro")
    tablet.turn_on()
    tablet.browse_web("https://www.example.com")
    tablet.turn_off()

    laptop = Laptop("HP", "Pavilion")
    laptop.turn_on()
    laptop.run_application("Microsoft Word")
    laptop.turn_off()
