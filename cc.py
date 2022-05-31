from PyQt6.QtWidgets import QApplication,QMainWindow,QLineEdit,QPushButton,QLabel,QComboBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QPropertyAnimation,QPoint,Qt
from sys import argv
from unit_convert import UnitConvert

class UnitConversion(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Unit Conversion")
        self.setFixedSize(600,600)
        self.setWindowIcon(QIcon("u.png"))
        self.setStyleSheet("background-color:white;")
        
        self.title = QLabel("Unit Conversion",self)
        self.title.setFixedSize(300,60)
        self.title.setStyleSheet("color:red;letter-spacing:10px;font-weight:bold;font-size:20px;")
        self.title_animation = QPropertyAnimation(self.title,b"pos")
        self.title_animation.setDuration(500)
        self.title_animation.setStartValue(QPoint(0,0))
        self.title_animation.setEndValue(QPoint(150,40))
        self.title_animation.start()
        
        self.data = UnitConvert.Data
        
        self.units = QComboBox(self)
        self.units.setGeometry(50,300,150,40)
        self.units.setStyleSheet("font-size:16px;color:green;background-color:black;")
        self.units.addItems(['Bytes','Kilobytes','MegaBytes','GigaBytes','TeraBytes','PetaBytes','NanoMetres','MicroMetres','MilliMetres','CentiMetres','inches','Feet', 'Meters','Yards','Kilometres','Miles', 'LightYears','Astronomical_Units', 'Parsec','NanoSeconds','MicroSeconds','MilliSeconds', 'Seconds','Minutes', 'Hours', 'Days', 'Weeks','Months', 'Years','Decades', 'Centurys','Grams','Kilograms','Ounces', 'Lbs', 'Pounds','Tons','Stones'])                    
        self.units.currentIndexChanged.connect(self.change)
        
        self.value = QLineEdit(self)
        self.value.setGeometry(250,300,100,40)
        self.value.setStyleSheet("color:blue;font-size:16px;")
        
        self.tounit = QComboBox(self)
        self.tounit.setGeometry(400,300,150,40)
        self.tounit.setStyleSheet("font-size:16px;color:green;background-color:black;")
        self.tounit.addItems([item.capitalize() for item in self.data if len(item) > 2 and list(self.data[item].items())[0][0] == list(self.data[self.units.currentText().lower()].items())[0][0] and list(self.data[item].items())[0][1] != list(self.data[self.units.currentText().lower()].items())[0][1]])          
                
        self.click_me = QPushButton("Convert",self)
        self.click_me.setGeometry(250,360,100,40)
        self.click_me.clicked.connect(self.outputer)
        
        self.output = QLabel(self)
        self.output.setFixedSize(400,60)
        self.output.setStyleSheet("color:brown;font-weight:bold;font-size:20px;")
        self.output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_animation = QPropertyAnimation(self.output,b"pos")
        self.output_animation.setDuration(250)
        self.output_animation.setStartValue(QPoint(0,600))
        self.output_animation.setEndValue(QPoint(100,450))
                
        self.show()
        
    def outputer(self):
        try:
            exec(f"self.output.setText(str(UnitConvert({self.units.currentText().lower()} = {float(self.value.text())}).{self.tounit.currentText().lower()}) + ' {self.tounit.currentText()}')")
        except Exception as e:
            self.output.setText(str(e))
        self.output_animation.start()

    def change(self,e):
        [self.tounit.removeItem(0) for index in range(self.tounit.count())]
        self.tounit.addItems([item.capitalize() for item in self.data if len(item) > 2 and list(self.data[item].items())[0][0] == list(self.data[self.units.currentText().lower()].items())[0][0] and list(self.data[item].items())[0][1] != list(self.data[self.units.currentText().lower()].items())[0][1]])

if __name__ == "__main__":
    application = QApplication(argv)
    uc = UnitConversion()
    application.exec()    
