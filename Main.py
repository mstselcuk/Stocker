from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QPoint
import sys
from PyQt5.QtWidgets import *
from Stocker import *

#-----------------------------------FRAMELESS WİNDOW-----------------------------------
class FramelessWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
#--------------------------------------------------------------------------------------
#-----------------------------------MOVE APP-------------------------------------------
        self.old_pos = self.pos()

    def mousePressEvent(self, event):
        # Başlık çubuğunu sürükleme işlemi için fare düğmesine basıldığında
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        # Fare sürüklendikçe pencereyi taşıma işlemi
        if event.buttons() == Qt.LeftButton:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()
#--------------------------------------------------------------------------------------
#-----------------------------------START APP------------------------------------------
app=QApplication(sys.argv)
window=FramelessWindow()
ui=Ui_Stocker()
ui.setupUi(window)
window.show()
#--------------------------------------------------------------------------------------



#-----------------------------------CLOSE APP------------------------------------------
sys.exit(app.exec_())