import ttkbootstrap as tb
from tkinter import ttk

from controllers.controller_absensi import AbsensiController


class DosenDashboard:

    def __init__(self, root, user, callback_logout):

        self.root = root
        self.user = user
        self.callback_logout = callback_logout

        # Bersihkan tampilan sebelumnya
        for widget in root.winfo_children():
            widget.destroy()

        # ==========================
        # MAIN CONTAINER
        # ==========================
        main_frame = tb.Frame(root)
        main_frame.pack(fill="both", expand=True)

        # ==========================
        # SIDEBAR
        # ==========================
        sidebar = tb.Frame(main_frame, width=250, bootstyle="dark")
        sidebar.pack(side="left", fill="y")

        tb.Label(
            sidebar,
            text="SISTEM\nABSENSI",
            font=("Segoe UI", 20, "bold"),
            bootstyle="inverse-dark"
        ).pack(pady=30)

        tb.Separator(sidebar).pack(fill="x", padx=10)

        tb.Button(
            sidebar,
            text="Dashboard",
            bootstyle="dark"
        ).pack(fill="x", padx=15, pady=10)

        tb.Button(
            sidebar,
            text="Data Absensi",
            bootstyle="dark"
        ).pack(fill="x", padx=15, pady=10)

        tb.Button(
            sidebar,
            text="Logout",
            bootstyle="danger",
            command=self.logout
        ).pack(fill="x", padx=15, pady=10)

        # ==========================
        # CONTENT
        # ==========================
        content = tb.Frame(main_frame, padding=20)
        content.pack(side="right", fill="both", expand=True)

        # HEADER
        tb.Label(
            content,
            text="Dashboard Dosen",
            font=("Segoe UI", 26, "bold")
        ).pack(anchor="w")

        tb.Label(
            content,
            text=f"Selamat Datang, {user[1]}",
            font=("Segoe UI", 12)
        ).pack(anchor="w")

        # ==========================
        # CARD STATISTIK
        # ==========================
        card_frame = tb.Frame(content)
        card_frame.pack(fill="x", pady=20)

        # Total Absensi
        card1 = tb.Labelframe(
            card_frame,
            text="Total Absensi",
            padding=20
        )
        card1.pack(side="left", padx=10)

        self.lbl_total = tb.Label(
            card1,
            text="0",
            font=("Segoe UI", 22, "bold")
        )
        self.lbl_total.pack()

        # Total Mahasiswa
        card2 = tb.Labelframe(
            card_frame,
            text="Mahasiswa Aktif",
            padding=20
        )
        card2.pack(side="left", padx=10)

        self.lbl_mahasiswa = tb.Label(
            card2,
            text="0",
            font=("Segoe UI", 22, "bold")
        )
        self.lbl_mahasiswa.pack()

        # ==========================
        # TOMBOL
        # ==========================
        btn_frame = tb.Frame(content)
        btn_frame.pack(fill="x", pady=10)

        tb.Button(
            btn_frame,
            text="REFRESH DATA",
            bootstyle="info",
            command=self.load_data
        ).pack(side="left", padx=5)

        tb.Button(
            btn_frame,
            text="EXPORT JSON",
            bootstyle="success"
        ).pack(side="left", padx=5)

        # ==========================
        # JUDUL TABEL
        # ==========================
        tb.Label(
            content,
            text="Data Absensi Mahasiswa",
            font=("Segoe UI", 16, "bold")
        ).pack(anchor="w", pady=10)

        # ==========================
        # TABEL
        # ==========================
        table_frame = tb.Frame(content)
        table_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(
            table_frame,
            columns=(
                "nama",
                "tanggal",
                "masuk",
                "pulang",
                "status"
            ),
            show="headings",
            height=20
        )

        self.tree.heading("nama", text="Nama")
        self.tree.heading("tanggal", text="Tanggal")
        self.tree.heading("masuk", text="Jam Masuk")
        self.tree.heading("pulang", text="Jam Pulang")
        self.tree.heading("status", text="Status")

        self.tree.column("nama", width=250)
        self.tree.column("tanggal", width=150)
        self.tree.column("masuk", width=150)
        self.tree.column("pulang", width=150)
        self.tree.column("status", width=120)

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

    def load_data(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        data = AbsensiController.semua_absensi()

        for row in data:
            self.tree.insert("", "end", values=row)

        self.lbl_total.config(text=str(len(data)))

        mahasiswa_unik = set()

        for row in data:
            mahasiswa_unik.add(row[0])

        self.lbl_mahasiswa.config(
            text=str(len(mahasiswa_unik))
        )

    def logout(self):
        self.callback_logout()