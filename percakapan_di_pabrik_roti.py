# Tugas Python OOP - Percakapan di Pabrik Roti
# Tema: pertemuan awal (wawancara) antara HRD dan calon karyawan


class Orang:
    # class attribute
    lokasi = "Pabrik Roti Sari Manis"

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bicara(self, kalimat):
        print(f"{self.nama}: {kalimat}")


class HRD(Orang):
    def __init__(self, nama, umur, jabatan):
        super().__init__(nama, umur)
        self.jabatan = jabatan

    def sambut(self, calon):
        self.bicara(f"Selamat pagi, {calon.nama}. Silakan duduk. Saya {self.nama}, {self.jabatan} di {Orang.lokasi}.")

    def tanya_perkenalan(self):
        self.bicara("Boleh ceritakan sedikit tentang diri Anda?")

    def tanya_posisi(self, calon):
        self.bicara(f"Anda melamar sebagai {calon.posisi}. Apa alasan Anda tertarik di bagian ini?")

    def tanya_pengalaman(self):
        self.bicara("Apakah Anda punya pengalaman kerja di bidang produksi makanan?")

    def tanya_shift(self):
        self.bicara("Pabrik kami beroperasi dengan sistem shift, termasuk shift pagi buta. Apakah Anda siap?")

    def tutup(self, calon):
        self.bicara(f"Terima kasih, {calon.nama}. Kami akan menghubungi Anda dalam 3 hari kerja.")


class CalonKaryawan(Orang):
    def __init__(self, nama, umur, posisi, pendidikan, pengalaman):
        super().__init__(nama, umur)
        self.posisi = posisi
        self.pendidikan = pendidikan
        self.pengalaman = pengalaman

    def salam(self, hrd):
        self.bicara(f"Selamat pagi, Bu {hrd.nama}. Terima kasih sudah memberi saya kesempatan.")

    def perkenalan(self):
        self.bicara(f"Saya {self.nama}, umur {self.umur} tahun, lulusan {self.pendidikan}.")

    def jawab_posisi(self):
        self.bicara(f"Saya suka proses pembuatan roti dan ingin belajar di bagian {self.posisi}.")

    def jawab_pengalaman(self):
        self.bicara(f"Saya punya pengalaman {self.pengalaman}.")

    def jawab_shift(self):
        self.bicara("Siap, Bu. Saya bisa bekerja di shift pagi maupun malam.")

    def pamit(self):
        self.bicara("Terima kasih kembali, Bu. Saya tunggu kabar baiknya.")


# ===== Program utama =====
hrd = HRD("Rina", 35, "Manajer HRD")
calon = CalonKaryawan("Budi", 22, "Operator Produksi", "SMK Teknik Pengolahan Pangan", "magang 6 bulan di toko roti")

print(f"=== Percakapan Awal di {Orang.lokasi} ===\n")
calon.salam(hrd)
hrd.sambut(calon)
hrd.tanya_perkenalan()
calon.perkenalan()
hrd.tanya_posisi(calon)
calon.jawab_posisi()
hrd.tanya_pengalaman()
calon.jawab_pengalaman()
hrd.tanya_shift()
calon.jawab_shift()
hrd.tutup(calon)
calon.pamit()
