class Player:
    def __init__(self, isim, can, guc):
        self.isim = isim
        self.can = can
        self.guc = guc

    def vur(self):
        print(f"{self.isim} {self.guc} güçle vurdu!")
        return self.guc

    def hasar_al(self, miktar):
        self.can -= miktar

        if self.can <= 0:
            self.can = 0
            print(f"{self.isim} öldü 💀")
        else:
            print(f"{self.isim} {miktar} hasar aldı. Kalan can: {self.can}")


p1 = Player("Ata", 100, 20)
p2 = Player("Aysima", 100, 30)

hasar = p1.vur()
p2.hasar_al(hasar)

print("Aysima can:", p2.can)
