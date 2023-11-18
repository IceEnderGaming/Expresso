import sys
import sqlite3

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import QtGui
from PyQt5 import uic


class Expresso(QMainWindow):
    def __init__(self):
        super().__init__()
        QtGui.QFontDatabase.addApplicationFont(fr'VAG_WORLD.ttf')
        uic.loadUi("main.ui", self)
        self.show_table()

    def load_from_db(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        coffee = [list(i) for i in cur.execute("SELECT * FROM coffee").fetchall()]
        return coffee

    def show_table(self):
        coffee = self.load_from_db()
        for k, i in enumerate(coffee):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(i[1::]):
                self.tableWidget.setItem(k, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Expresso()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
