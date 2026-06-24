import ttkbootstrap as tb
from tkinter import messagebox

from controllers.controller_auth import AuthController


class LoginView:

    def __init__(self, root, callback):

        self.root = root
        self.callback = callback

        # Container utama
        self.container = tb.Frame(root)
        self.container.pack(fill="both", expand=True)

        # Card login
        self.frame = tb.Labelframe(
            self.container,
            text=" LOGIN SISTEM ",
            padding=30
        )

        self.frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # Judul
        tb.Label(
            self.frame,
            text="SISTEM ABSENSI KAMPUS",
            font=("Segoe UI", 20, "bold")
        ).pack(pady=10)

        tb.Label(
            self.frame,
            text="Login Mahasiswa & Dosen",
            font=("Segoe UI", 10)
        ).pack(pady=(0, 20))

        # Username
        tb.Label(
            self.frame,
            text="Username"
        ).pack(anchor="w")

        self.username = tb.Entry(
            self.frame,
            width=35
        )

        self.username.pack(pady=5)

        # Password
        tb.Label(
            self.frame,
            text="Password"
        ).pack(anchor="w")

        self.password = tb.Entry(
            self.frame,
            width=35,
            show="*"
        )

        self.password.pack(pady=5)

        # Tombol Login
        tb.Button(
            self.frame,
            text="LOGIN",
            bootstyle="primary",
            command=self.do_login
        ).pack(
            fill="x",
            pady=20
        )

    def do_login(self):

        username = self.username.get()
        password = self.password.get()

        user = AuthController.login(
            username,
            password
        )

        if user:

            self.container.destroy()

            self.callback(user)

        else:

            messagebox.showerror(
                "Login Gagal",
                "Username atau Password salah!"
            )