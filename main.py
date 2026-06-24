import ttkbootstrap as tb

from database import init_database
from database import insert_default_data

from views.view_login import LoginView
from views.view_mahasiswa_dashboard import MahasiswaDashboard
from views.view_dosen_dashboard import DosenDashboard


class AbsensiApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Sistem Absensi Kampus")

        self.show_login()

    def show_login(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        LoginView(
            self.root,
            self.login_success
        )

    def login_success(self, user):

        role = user[4]

        if role == "mahasiswa":

            MahasiswaDashboard(
                self.root,
                user,
                self.show_login
            )

        elif role == "dosen":

            DosenDashboard(
                self.root,
                user,
                self.show_login
            )


if __name__ == "__main__":

    init_database()
    insert_default_data()

    root = tb.Window(
    themename="minty"
)
    

    root.title("Sistem Absensi Kampus")
    root.geometry("1200x700")
    root.resizable(False, False)

    app = AbsensiApp(root)

    root.mainloop()