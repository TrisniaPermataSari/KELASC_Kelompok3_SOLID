from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def makan(self):
        pass


class HewanTerbang(Hewan):
    def terbang(self):
        print(f"{self.nama} sedang terbang.")


class Burung(HewanTerbang):
    def makan(self):
        print(f"{self.nama} sedang makan.")


class Singa(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan.")