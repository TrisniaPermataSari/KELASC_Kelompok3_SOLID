from Hewan import Burung, Singa
from Kandang import Kandang
from Kebunbinatang import KebunBinatang

kandang = Kandang()

burung = Burung("Elang")
singa = Singa("Simba")

kandang.tambah_hewan(burung)
kandang.tambah_hewan(singa)

zoo = KebunBinatang(kandang)
zoo.rawat_semua_hewan()