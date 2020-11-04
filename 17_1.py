class Gun:
    def __init__(self, magazins, bullets):
        self.magazins = magazins
        self.bullets = bullets
        self.bull_in_mag = bullets

    def getMagazinsAmount(self):
        print('количество магазинов %s ' % self.magazins)

    def getBulletsAmount(self):
        print('количество патронов %s' % self.bull_in_mag)

    def reload(self):
        self.magazins -= 1
        self.bull_in_mag = self.bullets
        if self.magazins == 0:
            raise Exception('OutOfMagazins')

    def takeAShot(self):
        if self.bull_in_mag > 0:
            self.bull_in_mag -= 1
        else:
            self.reload()


gun = Gun(2, 3)
gun.takeAShot()
gun.takeAShot()
gun.getBulletsAmount()
gun.getMagazinsAmount()
gun.reload()
gun.takeAShot()
gun.takeAShot()
gun.takeAShot()
gun.getBulletsAmount()
gun.getMagazinsAmount()
gun.takeAShot()