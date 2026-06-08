from hewan import HewanTerbang

class KebunBinatang:
    def __init__(self, kandang):
        self.kandang = kandang
    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            if isinstance(hewan, HewanTerbang):
                hewan.terbang()