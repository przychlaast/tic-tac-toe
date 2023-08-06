import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg

import sys
#!/usr/bin/env python

class Gra(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.setWindowTitle('Kółko i krzyżyk')
        self.plansza()
        self.ruchy = 0


    def plansza(self):
        layout = qtw.QGridLayout(self)
        self.przyciski = []
        for y in range(3):
            rzad = []
            for x in range(3):
                przycisk = qtw.QPushButton()
                layout.addWidget(przycisk,y,x)
                przycisk.setFixedSize(110,110)
                przycisk.setFont(qtg.QFont("Arial",30))
                przycisk.clicked.connect(self.akcja)
                rzad.append(przycisk)
            self.przyciski.append(rzad)

        self.wyniki = qtw.QLabel()
        layout.addWidget(self.wyniki,4,0,1,3)
        self.wyniki.setText("Ruch gracza O")
        self.wyniki.setAlignment(qtc.Qt.AlignCenter)
        self.wyniki.setFont(qtg.QFont("Arial",30))

        restart = qtw.QPushButton("Restart")
        restart.setFixedSize(100, 50)
        layout.addWidget(restart, 3, 0, 1, 3)
        restart.clicked.connect(self.restart)

    def restart(self):
        for y in range(3):
            for x in range(3):
                self.przyciski[y][x].setText('')
                self.przyciski[y][x].setEnabled(True)
        self.ruchy = 0
        self.wyniki.setText("Ruch gracza O")

    def akcja(self):
        przycisk = self.sender()
        przycisk.setEnabled(False)

        if self.ruchy % 2 == 0:
            przycisk.setText("O")
            self.wyniki.setText("Ruch gracza X")
        else:
            przycisk.setText("X")
            self.wyniki.setText("Ruch gracza O")
        self.ruchy += 1

        koniec = False

        for n in range(3):
            if self.przyciski[n][0].text() == self.przyciski[n][1].text() == self.przyciski[n][2].text() != '':
                self.wyniki.setText(f'Wygrywa gracz {self.przyciski[n][0].text()}')
                koniec = True
                break
            if self.przyciski[0][n].text() == self.przyciski[1][n].text() == self.przyciski[2][n].text() != '':
                self.wyniki.setText(f'Wygrywa gracz {self.przyciski[0][n].text()}')
                koniec = True
                break
        if self.przyciski[0][0].text() == self.przyciski[1][1].text() == self.przyciski[2][2].text() != '':
            self.wyniki.setText(f'Wygrywa gracz {self.przyciski[0][0].text()}')
            koniec = True
        elif self.przyciski[0][2].text() == self.przyciski[1][1].text() == self.przyciski[2][0].text() != '':
            self.wyniki.setText(f'Wygrywa gracz {self.przyciski[0][2].text()}')
            koniec = True
        if not koniec and self.ruchy == 9:
            self.wyniki.setText('Remis')
        elif koniec:
            for y in range(3):
                for x in range(3):
                    self.przyciski[y][x].setEnabled(False)


def main():

    app = qtw.QApplication(sys.argv)
    gra = Gra()

    gra.show()
    app.exec()


if __name__ == '__main__':
    main()


