from PySide2 import QtWidgets
import calculator
import math


class Calculator(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.someMulOperator = ''
        self.someAdOperator = ''

        self.sumInMemory = 0.0
        self.mulInMemory = 0.0
        self.waitingForOperand = True

        self.ui = calculator.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.zero.clicked.connect(self.digitClicked)
        self.ui.one.clicked.connect(self.digitClicked)
        self.ui.two.clicked.connect(self.digitClicked)
        self.ui.three.clicked.connect(self.digitClicked)
        self.ui.four.clicked.connect(self.digitClicked)
        self.ui.five.clicked.connect(self.digitClicked)
        self.ui.six.clicked.connect(self.digitClicked)
        self.ui.seven.clicked.connect(self.digitClicked)
        self.ui.eight.clicked.connect(self.digitClicked)
        self.ui.nine.clicked.connect(self.digitClicked)
        self.ui.percent.clicked.connect(self.OperatorClicked) #%
        self.ui.degree.clicked.connect(self.OperatorClicked) #^2
        self.ui.divide.clicked.connect(self.mulClicked) #/
        self.ui.minus.clicked.connect(self.sumClicked) #-
        self.ui.mult.clicked.connect(self.mulClicked) #*
        self.ui.oneDelX.clicked.connect(self.OperatorClicked) #1/X
        self.ui.plus.clicked.connect(self.sumClicked) #+
        self.ui.plusAndMinus.clicked.connect(self.plusAndMinusClicked) #+/-
        self.ui.square.clicked.connect(self.OperatorClicked) #x^1/2
        self.ui.CE.clicked.connect(self.clearLast) #CE
        self.ui.C.clicked.connect(self.clearAll) #c
        self.ui.backspace.clicked.connect(self.backspaceClicked) #<-
        self.ui.point.clicked.connect(self.pointClicked) #,
        self.ui.equal.clicked.connect(self.equalClicked) #=


    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.ui.lineEdit.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.ui.lineEdit.clear()
            self.waitingForOperand = False

        self.ui.lineEdit.setText(self.ui.lineEdit.text() + str(digitValue))

    def stopOperation(self):
        self.clearAll()
        self.ui.lineEdit.setText("ошибка")

    def OperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.ui.lineEdit.text())

        if clickedOperator == "X^(1/2)":
            if operand < 0.0:
                self.stopOperation()
                return

            result = math.sqrt(operand)

        elif clickedOperator == "1/x":
            if operand == 0.0:
                self.stopOperation()
                return

            result = 1.0 / operand

        elif clickedOperator == "X^2":
            result = operand ** 2


        elif clickedOperator == "%":
            result = operand / 100


        self.ui.lineEdit.setText(str(result))
        self.waitingForOperand = True

    def pointClicked(self):
        if self.waitingForOperand:
            self.ui.lineEdit.setText('0')

        if "." not in self.ui.lineEdit.text():
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + ".")

        self.waitingForOperand = False

    def plusAndMinusClicked(self):
        text = self.ui.lineEdit.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.ui.lineEdit.setText(text)


    def backspaceClicked(self):
        if self.waitingForOperand:
            return

        text = self.ui.lineEdit.text()[:-1]
        if not text:
            text = '0'
            self.waitingForOperand = True

        self.ui.lineEdit.setText(text)


    def clearLast(self):
        if self.waitingForOperand:
            return

        self.ui.lineEdit.setText('0')
        self.waitingForOperand = True

    def clearAll(self):
        self.sumInMemory = 0.0
        self.mulInMemory = 0.0
        self.someAdOperator = ''
        self.someMulOperator = ''
        self.ui.lineEdit.setText('0')
        self.waitingForOperand = True


    def sumClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.ui.lineEdit.text())


        if self.someAdOperator:
            self.ui.lineEdit.setText(str(self.sumInMemory))
        else:
            self.sumInMemory = operand

        self.someAdOperator = clickedOperator
        self.waitingForOperand = True

    def mulClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.ui.lineEdit.text())

        if self.someMulOperator:
            self.ui.lineEdit.setText(str(self.mulInMemory))
        else:
            self.mulInMemory = operand

        self.someMulOperator = clickedOperator
        self.waitingForOperand = True

    def equalClicked(self):
        operand = float(self.ui.lineEdit.text())

        if self.someMulOperator:
            if self.calculate(operand, self.someMulOperator):
                operand = self.mulInMemory
                self.mulInMemory = 0.0
                self.someMulOperator = ''

        if self.someAdOperator:
            if self.calculate(operand, self.someAdOperator):
                self.someAdOperator = ''

        else:
            self.sumInMemory = operand

        self.ui.lineEdit.setText(str(self.sumInMemory))
        self.sumInMemory = 0.0
        self.waitingForOperand = True


    def calculate(self, rightOperand, operator):
        if operator == "+":
            self.sumInMemory += rightOperand

        elif operator == "-":
            self.sumInMemory -= rightOperand

        elif operator == "*":
            self.mulInMemory *= rightOperand

        elif operator == "/":
            if rightOperand == 0.0:
                return False

            self.mulInMemory /= rightOperand
        return True


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Calculator()
    window.show()

    app.exec_()