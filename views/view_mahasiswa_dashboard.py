import ttkbootstrap as tb
from tkinter import ttk, messagebox
from datetime import datetime

from controllers.controller_absensi import AbsensiController


class MahasiswaDashboard:

    def __init__(self, root, user, logout_callback):

        self.root = root
        self.user = user
        self.logout_callback = logout_callback

        # Bersihkan halaman sebelumnya
        for widget in root.winfo_children():
            widget.destroy()

        # ==========================
        # MAIN FRAME
        # ==========================
        main_frame = tb.Frame(root)
        main_frame.pack(fill="both", expand=True)

        # ==========================
        # SIDEBAR
        # ==========================
        sidebar = tb.Frame(main_frame, width=250, bootstyle="primary")
        sidebar.pack(side="left", fill="y")

        tb.Label(
            sidebar,
            text="🎓\nSISTEM\nABSENSI",
            font=("Segoe UI", 20, "bold"),
            foreground="white"
        ).pack(pady=30)

        tb.Separator(sidebar).pack(fill="x", padx=15)

        tb.Button(
            sidebar,
            text="🏠 Dashboard",
            bootstyle="primary-outline"
        ).pack(fill="x", padx=15, pady=10)

        tb.Button(
            sidebar,
            text="📋 Riwayat Absensi",
            bootstyle="primary-outline"
        ).pack(fill="x", padx=15, pady=10)

        tb.Button(
            sidebar,
            text="🚪 Logout",
            bootstyle="danger",
            command=self.logout
        ).pack(fill="x", padx=15, pady=10)

        # ==========================
        # CONTENT
        # ==========================
        content = tb.Frame(main_frame, padding=20)
        content.pack(side="right", fill="both", expand=True)

        # ==========================
        # HEADER
        # ==========================
        header = tb.Frame(content)
        header.pack(fill="x")

        tb.Label(
            header,
            text="Dashboard Mahasiswa",
            font=("Segoe UI", 26, "bold")
        ).pack(anchor="w")

        tb.Label(
            header,
            text=f"Selamat Datang, {user[1]}",
            font=("Segoe UI", 12)
        ).pack(anchor="w")

        self.lbl_jam = tb.Label(
            header,
            font=("Segoe UI", 11)
        )
        self.lbl_jam.pack(anchor="w")

        self.update_jam()

        # ==========================
        # CARD STATISTIK
        # ==========================
        card_frame = tb.Frame(content)
        card_frame.pack(fill="x", pady=20)

        card1 = tb.Labelframe(
            card_frame,
            text="Total Absensi",
            padding=20,
            bootstyle="success"
        )
        card1.pack(side="left", padx=10)

        self.lbl_total = tb.Label(
            card1,
            text="0",
            font=("Segoe UI", 24, "bold")
        )
        self.lbl_total.pack()

        card2 = tb.Labelframe(
            card_frame,
            text="Status Mahasiswa",
            padding=20,
            bootstyle="info"
        )
        card2.pack(side="left", padx=10)

        tb.Label(
            card2,
            text="AKTIF",
            font=("Segoe UI", 20, "bold")
        ).pack()

        # ==========================
        # TOMBOL ABSENSI
        # ==========================
        btn_frame = tb.Frame(content)
        btn_frame.pack(fill="x", pady=10)

        tb.Button(
            btn_frame,
            text="✅ ABSEN MASUK",
            bootstyle="success",
            width=25,
            command=self.absen_masuk
        ).pack(side="left", padx=5)

        tb.Button(
            btn_frame,
            text="❌ ABSEN PULANG",
            bootstyle="danger",
            width=25,
            command=self.absen_pulang
        ).pack(side="left", padx=5)

        # ==========================
        # JUDUL TABEL
        # ==========================
        tb.Label(
            content,
            text="Riwayat Absensi",
            font=("Segoe UI", 16, "bold")
        ).pack(anchor="w", pady=10)

        # ==========================
        # TABLE
        # ==========================
        table_frame = tb.Frame(content)
        table_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("tgl", "masuk", "pulang", "status"),
            show="headings",
            height=18
        )

        self.tree.heading("tgl", text="Tanggal")
        self.tree.heading("masuk", text="Jam Masuk")
        self.tree.heading("pulang", text="Jam Pulang")
        self.tree.heading("status", text="Status")

        self.tree.column("tgl", width=180)
        self.tree.column("masuk", width=180)
        self.tree.column("pulang", width=180)
        self.tree.column("status", width=150)

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        tb.Label(
            content,
            text="© 2026 Sistem Absensi Kampus",
            font=("Segoe UI", 9)
        ).pack(pady=5)

        self.load_data()

    def update_jam(self):

        now = datetime.now()

        self.lbl_jam.config(
            text=now.strftime("%d-%m-%Y %H:%M:%S")
        )

        self.root.after(
            1000,
            self.update_jam
        )

    def load_data(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        data = AbsensiController.riwayat(
            self.user[0]
        )

        self.lbl_total.config(
            text=str(len(data))
        )

        for row in data:
            self.tree.insert("", "end", values=row)

    def absen_masuk(self):

        hasil = AbsensiController.absen_masuk(
            self.user[0]
        )

        if hasil:

            messagebox.showinfo(
                "Berhasil",
                "Absen masuk berhasil"
            )

        else:

            messagebox.warning(
                "Gagal",
                "Anda sudah absen hari ini"
            )

        self.load_data()

    def absen_pulang(self):

        hasil = AbsensiController.absen_pulang(
            self.user[0]
        )

        if hasil:

            messagebox.showinfo(
                "Berhasil",
                "Absen pulang berhasil"
            )

        else:

            messagebox.warning(
                "Gagal",
                "Anda belum absen masuk atau sudah absen pulang"
            )

        self.load_data()

    def logout(self):

        if messagebox.askyesno(
            "Logout",
            "Yakin ingin logout?"
        ):
            self.logout_callback()