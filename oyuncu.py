class Player:
    def __init__(self, isim, can, guc):
        self.isim = isim
        self.can = can
        self.guc = guc

    def hasar_al(self, miktar):
        self.can -= miktar

        if self.can <= 0:
            self.can = 0
            print(f"{self.isim} öldü 💀")
        else:
            print(f"{self.isim} {miktar} hasar aldı. Kalan can: {self.can}")

    def vur(self, target):

        if self == target:
            print("Kendinize vuramazsiniz.")
            return

        elif self.can <=0:
            print(f"{self.isim} zaten ölü, saldıramaz.")
            return
        
        else:

            if target.can<=0:
                print(f"{target.isim} zaten ölü.")
                return
            else:

                print(f"{self.isim} {self.guc} hasar verdi.")
                target.hasar_al(self.guc)


    def heal(self,arttir=20):
        if self.can >=100:
            print(f"{self.isim} zaten caniniz full. ")
            return
        else:
            self.can += arttir


class Mage(Player):
    def __init__(self, isim, can, guc,mana):
        super().__init__(isim, can, guc)
        self.mana = mana

    def vur(self,target):
        if self == target:
            print("Kendinize vuramazsiniz.")
            return
         
        if self.can <= 0:
            print("Ölüsünüz.")
            return
        
        if target.can<=0:
            print(f"{target.isim} ölü zaten.")
            return
        
        if self.mana>=10:
            print(f"{self.isim} {self.guc*2} hasar verdi.")
            target.hasar_al(self.guc*2)
            self.mana -=10

        else:
            super().vur(target)

    def heal(self,arttır=20):
        if self.mana>=15:
            if self.can>=100:
                print(f"{self.isim} caniniz zaten full.")
            else:
                self.can+=arttır
                self.mana -=10
        else:
            print(f"{self.isim} yeterli mananiz yok.")



class Warrior(Player):
    def __init__(self, isim, can, guc,kalkan):
        super().__init__(isim, can, guc)
        self.kalkan = kalkan

    def vur(self,target):
        if self == target:
            print("Kendinize vuramazsiniz.")
            return
         
        if self.can <= 0:
            print("Ölüsünüz.")
            return
        
        if target.can<=0:
            print(f"{target.isim} ölü zaten.")
            return
        
        else:
            super().vur(target)

    def hasar_al(self, miktar):

        if self.kalkan > 0:
            absorbed = min(self.kalkan, miktar)
            self.kalkan -= absorbed
            miktar -= absorbed
            print(f"{self.isim} kalkanı {absorbed} hasarı engelledi.")

        if miktar > 0:
            self.can -= miktar

        if self.can <= 0:
            self.can = 0
            print(f"{self.isim} öldü 💀")
        else:
            print(f"{self.isim} {miktar} hasar aldı. Kalan can: {self.can}")

    
        

p1 = Player("Ata", 100, 20)
m1 = Mage("Aysima", 80, 15, 25)
w1 = Warrior("Ahmet", 150, 35, 40)

m1.vur(w1)
m1.vur(w1)
m1.vur(w1)

print(w1.can)