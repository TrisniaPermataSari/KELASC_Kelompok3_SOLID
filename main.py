from abc import ABC, abstractmethod


# TRISNIA - SRP
class Hewan(ABC):
    def __init__(self, nama):
        self.nama = nama


    @abstractmethod
    def makan(self):
        pass


# MADA - OCP
# SAFIRA - ISP
class HewanTerbang(Hewan):
    def terbang(self):
        print(f"{self.nama} sedang terbang.")


# GISMA - LSP
class Burung(HewanTerbang):
    def makan(self):
        print(f"{self.nama} sedang makan.")
class Singa(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan.")


# TRISNIA - SRP
class Kandang:
    def __init__(self):
        self.hewan_list = []


    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)


    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")


# AKBAR - DIP
class KebunBinatang:
    def __init__(self, kandang):
        self.kandang = kandang


    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()


            if isinstance(hewan, HewanTerbang):
                hewan.terbang()


kandang = Kandang()
burung = Burung("Elang")
singa = Singa("Simba")

kandang.tambah_hewan(burung)
kandang.tambah_hewan(singa)

zoo = KebunBinatang(kandang)
zoo.rawat_semua_hewan()
