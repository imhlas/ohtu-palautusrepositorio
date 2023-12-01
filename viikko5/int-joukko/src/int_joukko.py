KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self._tarkista_arvo(kapasiteetti, KAPASITEETTI)
        self.kasvatuskoko = self._tarkista_arvo(kasvatuskoko, OLETUSKASVATUS)

        self.alkiot = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def _tarkista_arvo(self, arvo, oletus):
        if arvo is None:
            return oletus
        if not isinstance(arvo, int) or arvo < 0:
            raise Exception("Virheellinen arvo")
        return arvo

    def kuuluu(self, n):
        return n in self.alkiot

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.alkiot[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.alkiot):
                self.kasvata()

            return True

        return False

    def kasvata(self):
        self.alkiot += [0] * self.kasvatuskoko

    def poista(self, n):
        if n in self.alkiot:
            kohta = self.alkiot.index(n)

            for j in range(kohta, self.alkioiden_lkm - 1):
                self.alkiot[j] = self.alkiot[j + 1]

            self.alkioiden_lkm -= 1
            self.alkiot[self.alkioiden_lkm] = 0
            return True

        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.alkiot[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.alkiot[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.alkiot[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.alkiot[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
