from abc import ABC, abstractmethod

# Abstraksi Hewan
class Hewan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def makan(self):
        pass

# Interface hewan yang bisa terbang
class BisaTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

# Implementasi hewan
class Burung(Hewan, BisaTerbang):
    def makan(self):
        print(f"{self.nama} sedang makan.")

    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Kucing(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan.")

# Abstraksi kandang
class IKandang(ABC):
    @abstractmethod
    def tambah_hewan(self, hewan):
        pass

    @abstractmethod
    def get_hewan(self):
        pass

# Implementasi kandang
class Kandang(IKandang):
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def get_hewan(self):
        return self.hewan_list

# Abstraksi kebun binatang
class KebunBinatang:
    def __init__(self, kandang: IKandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.get_hewan():
            hewan.makan()

            if isinstance(hewan, BisaTerbang):
                hewan.terbang()

# Pemanggilan program
kandang = Kandang()

burung = Burung("Elang")
kucing = Kucing("joni")

kandang.tambah_hewan(burung)
kandang.tambah_hewan(kucing)

kebun_binatang = KebunBinatang(kandang)
kebun_binatang.rawat_semua_hewan()