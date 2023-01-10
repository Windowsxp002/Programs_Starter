import configparser
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QToolTip, QDialog, QMessageBox
from PyQt5.QtGui import QCursor
import MainWindow
import ConfigName
from configparser import ConfigParser
import os


class ConfigDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ConfigName.Ui_Dialog()
        self.ui.setupUi(self)
        # 初始化
        self.init_ui()

    def init_ui(self):
        # 初始化方法，这里可以写按钮绑定等的一些初始函数
        self.ui.Button_Ok.clicked.connect(self.on_ok)
        # show
        self.show()

    def on_ok(self):
        if self.ui.lineEdit.text() == '':
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '配置文件名无效')
            msg_box.exec_()
            return
        section_name = self.ui.lineEdit.text()
        config = ConfigParser()
        config.read('config.ini')
        if config.has_section(section_name):
            # 总是复写已存在的配置文件
            config.remove_section(section_name)
        else:
            config.add_section(section_name)
        for row in range(self.parent().ui.tableWidget.rowCount()):
            item0 = self.parent().ui.tableWidget.item(row, 0)
            item1 = self.parent().ui.tableWidget.item(row, 1)
            key = item0.text().replace(':', '_')
            if item1:
                value = item1.text().replace(':', '_')
            else:
                value = ''
            config.set(section_name, key, value)
        with open('config.ini', 'w') as f:
            config.write(f)
        self.parent().on_read()
        self.close()


class ProgramStarter(QMainWindow):
    def __init__(self):
        self.deleteBtn = None
        self.browserBtn = None
        self.app = QApplication(sys.argv)
        super().__init__()
        self.ui = MainWindow.Ui_Dialog()
        self.ui.setupUi(self)
        # 初始化
        self.init_ui()

    # ui初始化
    def init_ui(self):
        # 初始化方法，这里可以写按钮绑定等的一些初始函数
        self.ui.tableWidget.verticalHeader().setHidden(1)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(['程序路径', '附加参数', '操作'])
        self.ui.tableWidget.setColumnWidth(0, int(self.ui.tableWidget.width() * 0.3))
        self.ui.tableWidget.setColumnWidth(1, int(self.ui.tableWidget.width() * 0.45))
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(2)
        self.setWindowTitle('程序启动器')
        config = ConfigParser()  # 创建对象
        config.read("config.ini", encoding="utf-8")
        secs = config.sections()
        for i in range(len(secs)):
            self.ui.comboBox.addItem(secs[i])
        # 事件绑定
        self.ui.tableWidget.setMouseTracking(True)
        self.ui.Button_add.clicked.connect(self.on_add)
        self.ui.Button_save.clicked.connect(self.on_save)
        self.ui.Button_read.clicked.connect(self.on_read)
        self.ui.Button_start.clicked.connect(self.on_start)
        self.ui.tableWidget.cellEntered.connect(self.on_show_tooltip)
        # show
        self.show()

    def button_for_row(self):
        widget = QtWidgets.QWidget()
        # 修改
        self.browserBtn = QtWidgets.QPushButton('浏览程序')
        self.browserBtn.setStyleSheet(''' text-align : center;
                                                  background-color : NavajoWhite;
                                                  height : 35px;
                                                  border-style: outset;
                                                  font : 16px  ''')

        # 删除
        self.deleteBtn = QtWidgets.QPushButton('删除')
        self.deleteBtn.setStyleSheet(''' text-align : center;
                                            background-color : LightCoral;
                                            height : 35px;
                                            border-style: outset;
                                            font : 16px; ''')
        # 绑定事件
        self.browserBtn.clicked.connect(self.on_browser_button)
        self.deleteBtn.clicked.connect(self.on_delete_button)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.browserBtn)
        layout.addWidget(self.deleteBtn)
        layout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(layout)
        return widget

    def on_add(self):
        count_number = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(count_number)
        self.ui.tableWidget.setCellWidget(count_number, 2, self.button_for_row())

    def on_add(self, program_name):
        count_number = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(count_number)
        self.ui.tableWidget.setCellWidget(count_number, 2, self.button_for_row())
        item = QTableWidgetItem(program_name)
        self.ui.tableWidget.setItem(count_number, 0, item)

    def on_save(self):
        config_dialog = ConfigDialog(self)
        config_dialog.exec()

    def on_read(self):
        self.ui.tableWidget.setRowCount(0)
        config = ConfigParser()  # 创建对象
        config.read("config.ini", encoding="utf-8")  # 读取配置文件，如果配置文件不存在则创建
        if self.ui.comboBox.currentText() != '':
            item_list = config.items(self.ui.comboBox.currentText())  # 获取指定节点的键值对
            for i in range(len(item_list)):
                count_number = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(count_number)
                self.ui.tableWidget.setCellWidget(count_number, 2, self.button_for_row())
                item = QTableWidgetItem(item_list[i][0].replace('_', ':'))
                self.ui.tableWidget.setItem(count_number, 0, item)
                item = QTableWidgetItem(item_list[i][1])
                self.ui.tableWidget.setItem(count_number, 1, item)

    def on_start(self):
        for row in range(self.ui.tableWidget.rowCount()):
            item0 = self.ui.tableWidget.item(row, 0).text()
            item1 = self.ui.tableWidget.item(row, 1).text()
            os.startfile(item0+' '+item1)

    def on_browser_button(self):
        file_dialog = QFileDialog()
        filenames = file_dialog.getOpenFileNames(file_dialog, "选择程序", "./", "Programs(*.exe)")
        if len(filenames[0]) == 0:
            return
        button = self.sender()
        item = QTableWidgetItem(filenames[0][0])
        if button:
            row = self.ui.tableWidget.indexAt(button.parent().pos()).row()
            # print(row)
            self.ui.tableWidget.setItem(row, 0, item)
            if len(filenames[0]) > 1:
                for i in range(len(filenames[0])):
                    print(filenames[0][i])
                    self.on_add(filenames[0][i])

    def on_delete_button(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget.indexAt(button.parent().pos()).row()
            self.ui.tableWidget.removeRow(row)

    def on_show_tooltip(self, row, column):
        item = self.ui.tableWidget.item(row, column)
        if item:
            QToolTip.showText(QCursor().pos(), item.text())


# 程序入口
if __name__ == '__main__':
    e = ProgramStarter()
    sys.exit(e.app.exec())
