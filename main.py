from __future__ import unicode_literals
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                            QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                            QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                            QVBoxLayout, QMainWindow)
from PyQt5.QtGui import QPalette, QColor
import sys
import youtube_dl
import os

def createFolderForTiff(folder_name, path):
    _fold_name = folder_name.replace(':', ' ').replace('.', ' ')
    _path = path


    if not(os.path.exists(_path+"/"+_fold_name)):
        os.chdir(_path)
        os.mkdir(_fold_name)
    else:
        print('Папка C:/'+folder_name+' уже существует!')


folder_names = ["downloaded"]
pathh = "C:/"

for name in folder_names:
    createFolderForTiff(name,pathh)


class App():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.setGeometry(50,50,400,500)
        self.window.setMaximumSize(400,500)
        self.window.setMinimumSize(400,500)
        self.window.setWindowTitle("Youtube Downloader")
        self.window.setStyleSheet("background-color: #2c3338;")
        self.window.setWindowIcon(QtGui.QIcon("img/youtube.ico"))

        self.frame = QtWidgets.QFrame(self.window)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setGeometry(0,120,1200,478)
        self.frame.setStyleSheet("background: rgba(0,0,0,0.0); border:none;")

        self.frame_title = QtWidgets.QFrame(self.window)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setGeometry(0,0,1200,100)
        self.frame_title.setStyleSheet("background: transparent; border:none;")

        self.logo_video = QtWidgets.QToolButton(self.frame)
        self.logo_video.setGeometry(10,50,80,50)
        self.logo_video.setIcon(QtGui.QIcon("img/play2.png"))
        self.logo_video.setIconSize(QtCore.QSize(16, 16))
        self.logo_video.setStyleSheet("background: #363b41; border-top-left-radius: 10px; border-bottom-left-radius: 10px;")
    
        self.video_input = QtWidgets.QLineEdit(self.frame)
        self.video_input.setGeometry(90, 50, 300,50)
        self.video_input.setStyleSheet("border-bottom-right-radius: 10px; border-top-right-radius: 10px; font-family: Trebuchet MS; font-size:18px; color:white; background: rgba(0,0,0,0.1);")
        self.video_input.setPlaceholderText("Enter URL here")

        self.button_confirm = QtWidgets.QPushButton(self.frame)
        self.button_confirm.setGeometry(10,110,380,50)
        self.button_confirm.setStyleSheet("QPushButton{background:#ea4c88; text-transform: uppercase; border-radius:10px; color:white; font-family: Trebuchet MS;\
        font-size:18px; font-weight:bold;}\n" "QPushButton:hover{background: #e6397b;}")
        self.button_confirm.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_confirm.setText("download")
        self.button_confirm.setIcon(QtGui.QIcon("img/download.ico"))
        self.button_confirm.setIconSize(QtCore.QSize(20, 20))
        self.button_confirm.clicked.connect(self.download_video)

        self.button_black = QtWidgets.QPushButton(self.frame)
        self.button_black.setGeometry(10,330, 40,40)
        self.button_black.setStyleSheet("QPushButton{background:#f774a7; border-top-left-radius: 10px; border-bottom-left-radius: 10px;}\n" "QPushButton:hover{background: #e6397b;}")
        self.button_black.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_black.setIcon(QtGui.QIcon("img/moon-theme.ico"))
        self.button_black.setIconSize(QtCore.QSize(30, 30))
        self.button_black.clicked.connect(self.moon_theme)

        self.button_white = QtWidgets.QPushButton(self.frame)
        self.button_white.setGeometry(52,330, 40,40)
        self.button_white.setStyleSheet("QPushButton{background:#f774a7; border-top-right-radius: 10px; border-bottom-right-radius: 10px;}\n" "QPushButton:hover{background: #e6397b;}")
        self.button_white.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_white.setIcon(QtGui.QIcon("img/light-theme.ico"))
        self.button_white.setIconSize(QtCore.QSize(30, 30))
        self.button_white.clicked.connect(self.sun_theme)

        self.return_video_text = QtWidgets.QLabel(self.frame)
        self.return_video_text.setGeometry(65,355,300,40)
        self.return_video_text.setStyleSheet("font-family: Trebuchet MS; font-size:12px; color:white;")

        self.window.show()
        sys.exit(self.app.exec_())


    def sun_theme(self):
        self.window.setStyleSheet("background-color: #74bbfc;")
        self.logo_video.setStyleSheet("background: #add8ff; border-top-left-radius: 10px; border-bottom-left-radius: 10px;")
        self.button_confirm.setStyleSheet("QPushButton{background:#42a4ff; text-transform: uppercase; border-radius:10px; color:white; font-family: Trebuchet MS;\
        font-size:18px; font-weight:bold;}\n" "QPushButton:hover{background: #2696ff;}")
        self.logo_video.setIcon(QtGui.QIcon("img/play3.png"))
        self.button_black.setStyleSheet("QPushButton{background:#42a4ff; border-top-left-radius: 10px; border-bottom-left-radius: 10px;}\n" "QPushButton:hover{background: #2696ff;}")
        self.button_white.setStyleSheet("QPushButton{background:#42a4ff; border-top-right-radius: 10px; border-bottom-right-radius: 10px;}\n" "QPushButton:hover{background: #2696ff;}")

    def moon_theme(self):
        self.window.setStyleSheet("background-color: #2c3337;")
        self.logo_video.setStyleSheet("background: #363b41; border-top-left-radius: 10px; border-bottom-left-radius: 10px;")
        self.button_confirm.setStyleSheet("QPushButton{background:#ea4c88; text-transform: uppercase; border-radius:10px; color:white; font-family: Trebuchet MS;\
        font-size:18px; font-weight:bold;}\n" "QPushButton:hover{background: #e6397b;}")
        self.logo_video.setIcon(QtGui.QIcon("img/play2.png"))
        self.button_black.setStyleSheet("QPushButton{background:#f774a7; border-top-left-radius: 10px; border-bottom-left-radius: 10px;}\n" "QPushButton:hover{background: #e6397b;}")
        self.button_white.setStyleSheet("QPushButton{background:#f774a7; border-top-right-radius: 10px; border-bottom-right-radius: 10px;}\n" "QPushButton:hover{background: #e6397b;}")

    def download_video(self):
        try:
            ydl_opts = {
                'outtmpl': 'c:/downloaded/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.video_input.text()])
            self.return_video_text.setText("The download was successful! Check the folder!")
        except:
            self.return_video_text.setText("The download was successful! Check the folder!")
            
    def clear_video(self):
        self.return_video_text.clear()
        self.video_input.clear()
App()