from datetime import datetime

from models.model_absensi import AbsensiModel


class AbsensiController:

    @staticmethod
    def absen_masuk(user_id):

        now = datetime.now()

        tanggal = now.strftime("%Y-%m-%d")
        jam = now.strftime("%H:%M:%S")

        cek = AbsensiModel.cek_absen_hari_ini(
            user_id,
            tanggal
        )

        if cek:
            return False

        AbsensiModel.absen_masuk(
            user_id,
            tanggal,
            jam
        )

        return True

    @staticmethod
    def absen_pulang(user_id):

        now = datetime.now()

        tanggal = now.strftime("%Y-%m-%d")
        jam = now.strftime("%H:%M:%S")

        cek_masuk = AbsensiModel.cek_absen_hari_ini(
            user_id,
            tanggal
        )

        if not cek_masuk:
            return False

        cek_pulang = AbsensiModel.cek_absen_pulang(
            user_id,
            tanggal
        )

        if cek_pulang:
            return False

        AbsensiModel.absen_pulang(
            user_id,
            tanggal,
            jam
        )

        return True

    @staticmethod
    def riwayat(user_id):
        return AbsensiModel.get_riwayat(user_id)

    @staticmethod
    def semua_absensi():
        return AbsensiModel.get_all_absensi()