from database import get_connection


class AbsensiModel:

    @staticmethod
    def absen_masuk(user_id, tanggal, jam):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO absensi(
            user_id,
            tanggal,
            jam_masuk,
            status
        )
        VALUES(?,?,?,?)
        """, (user_id, tanggal, jam, "HADIR"))

        conn.commit()
        conn.close()

    @staticmethod
    def absen_pulang(user_id, tanggal, jam):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE absensi
        SET jam_pulang=?
        WHERE user_id=? AND tanggal=?
        """, (jam, user_id, tanggal))

        conn.commit()
        conn.close()

    @staticmethod
    def get_riwayat(user_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT tanggal,
               jam_masuk,
               jam_pulang,
               status
        FROM absensi
        WHERE user_id=?
        ORDER BY id DESC
        """, (user_id,))

        data = cursor.fetchall()

        conn.close()

        return data

    @staticmethod
    def get_all_absensi():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            users.nama,
            absensi.tanggal,
            absensi.jam_masuk,
            absensi.jam_pulang,
            absensi.status
        FROM absensi
        JOIN users
        ON absensi.user_id = users.id
        ORDER BY absensi.id DESC
        """)

        data = cursor.fetchall()

        conn.close()

        return data