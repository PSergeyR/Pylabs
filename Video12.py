# Описать в терминах ООП

class Aero:
    def __init__(self, name, model, weight):
        self.name = name
        self.model = model
        self.weight = weight

    def start(self):
        print(self.name, self.model, "Старт произведен")

    def stop(self):
        print(self.name, self.model, "Двигатель заглушен")

aero_1 = Aero("Cessna", 182, 894)
print(aero_1.name, aero_1.model)


aero_2 = Aero("Cessna", 206, 951)
print(aero_2.name, aero_1.model)

aero_1.start()
aero_2.stop()
