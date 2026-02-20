import sys
import os
import logging
from PyQt5 import QtWidgets, QtGui
from ui.main_window import MainWindow

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    # 设置应用程序字体
    font = QtGui.QFont("Microsoft YaHei", 12)
    app.setFont(font)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()