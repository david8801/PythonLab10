class Juicer:
    number_of_juicers = 0

    def __init__(self, color="unknown", max_amount_of_juice="unknown", energy_usage="unknown", producer="unknown", price="unknown", weight="unknown", height="unknown"):
        Juicer.number_of_juicers += 1
        self.color = color
        self.max_amount_of_juice = max_amount_of_juice
        self.energy_usage = energy_usage
        self.producer = producer
        self.price = price
        self.weight = weight
        self.height = height

    def __del__(self):
        print("%s was deleted" % self.producer)
        Juicer.number_of_juicers -= 1

    def __str__(self):
        return "color: " + self.color \
            + ", max amount of juice produced by juicer in liters by hour: " + self.max_amount_of_juice \
            + ", amount of energy used by juicer(in kilowatt): " + self.energy_usage \
            + ", is produced by: " + self.producer \
            + ", price: $" + self.price \
            + ", it weights: " + self.weight \
            + ", height: " + self.height


    @staticmethod
    def get_number_of_juicers():
        return Juicer.number_of_juicers

blizzard = Juicer(color="green", max_amount_of_juice="12", energy_usage="120", producer="blizzard", price="250", weight="7", height="30")
print(blizzard)
print("\n")
print('Number of juicers: ', Juicer.get_number_of_juicers())
valve = Juicer(color="red", max_amount_of_juice="15", energy_usage="220", producer="valve", price="400", weight="10", height="50")
print(valve)
print("\n")
print('Number of juicers: ', Juicer.get_number_of_juicers())
epic = Juicer(color="yellow", max_amount_of_juice="10", energy_usage="150", producer="epic", price="340", weight="5", height="40")
print(epic)
print("\n")
print('Number of juicers: ', Juicer.get_number_of_juicers())
