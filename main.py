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

class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self, kandang):
        self.kandang = Kandang()

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()

            if isinstance(hewan, HewanTerbang):
                hewan.terbang()

kandang = Kandang()
zoo = KebunBinatang(kandang)