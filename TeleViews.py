# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from sys import argv, exit
from qdarkstyle import load_stylesheet_pyqt5
from re import search
from threading import Thread
from time import sleep
from os import makedirs
import requests

is_api = False
counter, sent, unknown, error, bad_proxy, timeout_error, spm = -1, 0, 0, 0, 0, 0, 0
logs_file = open('logs.txt', 'a+')
proxies_list = []

try: makedirs("img")
except FileExistsError: pass


def download_pic(pic: str, url: str):
    try:
        with open(pic, 'wb') as save: save.write(requests.get(url).content)
    except Exception as ex: logs_file.write(str(f"Error: {ex}\n"))


download_pic('img/icon.png', 'https://i.imgur.com/CZQl4Be.png')
download_pic('img/ad1.png', 'https://i.imgur.com/0oSZaKa.png')
download_pic('img/ad2.png', 'https://i.imgur.com/i0MciUp.png')
icon_photo, ad_1_photo, ad_2_photo = "img/icon.png", "img/ad1.png", "img/ad2.png"


class GUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_photo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        MainWindow.resize(631, 642)
        MainWindow.setFixedSize(631, 642)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(30, 595, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.textbox_channel = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox_channel.setGeometry(QtCore.QRect(30, 96, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.textbox_channel.setFont(font)
        self.textbox_channel.setText("")
        self.textbox_channel.setObjectName("textbox_channel")
        self.spinBox_timeout = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_timeout.setGeometry(QtCore.QRect(110, 332, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.spinBox_timeout.setFont(font)
        self.spinBox_timeout.setMinimum(3)
        self.spinBox_timeout.setMaximum(50)
        self.spinBox_timeout.setProperty("value", 15)
        self.spinBox_timeout.setObjectName("spinBox_timeout")
        self.comboBox_proxytype = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_proxytype.setGeometry(QtCore.QRect(110, 372, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.comboBox_proxytype.setFont(font)
        self.comboBox_proxytype.setObjectName("comboBox_proxytype")
        self.comboBox_proxytype.addItem("")
        self.comboBox_proxytype.addItem("")
        self.comboBox_proxytype.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 336, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 376, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 136, 301, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.spinBox_range_1 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_range_1.setGeometry(QtCore.QRect(80, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.spinBox_range_1.setFont(font)
        self.spinBox_range_1.setMinimum(1)
        self.spinBox_range_1.setMaximum(9999)
        self.spinBox_range_1.setProperty("value", 1)
        self.spinBox_range_1.setObjectName("spinBox_range_1")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(170, 90, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.spinBox_range_2 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_range_2.setGeometry(QtCore.QRect(200, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.spinBox_range_2.setFont(font)
        self.spinBox_range_2.setMinimum(1)
        self.spinBox_range_2.setMaximum(9999)
        self.spinBox_range_2.setProperty("value", 100)
        self.spinBox_range_2.setObjectName("spinBox_range_2")
        self.radioButton_post_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_post_2.setGeometry(QtCore.QRect(200, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.radioButton_post_2.setFont(font)
        self.radioButton_post_2.setObjectName("radioButton_post_2")
        self.radioButton_post_1 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_post_1.setGeometry(QtCore.QRect(100, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.radioButton_post_1.setFont(font)
        self.radioButton_post_1.setChecked(True)
        self.radioButton_post_1.setObjectName("radioButton_post_1")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textbox_post = QtWidgets.QLineEdit(self.frame)
        self.textbox_post.setGeometry(QtCore.QRect(20, 50, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.textbox_post.setFont(font)
        self.textbox_post.setText("")
        self.textbox_post.setObjectName("textbox_post")
        self.spinBox_threads = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_threads.setGeometry(QtCore.QRect(110, 292, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.spinBox_threads.setFont(font)
        self.spinBox_threads.setMinimum(15)
        self.spinBox_threads.setMaximum(555)
        self.spinBox_threads.setSingleStep(10)
        self.spinBox_threads.setProperty("value", 50)
        self.spinBox_threads.setObjectName("spinBox_threads")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 296, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 416, 301, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.radioButton_proxy_1 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_proxy_1.setGeometry(QtCore.QRect(130, 12, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.radioButton_proxy_1.setFont(font)
        self.radioButton_proxy_1.setChecked(True)
        self.radioButton_proxy_1.setObjectName("radioButton_proxy_1")
        self.radioButton_proxy_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_proxy_2.setGeometry(QtCore.QRect(200, 12, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.radioButton_proxy_2.setFont(font)
        self.radioButton_proxy_2.setObjectName("radioButton_proxy_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(28, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_browse = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_browse.setGeometry(QtCore.QRect(24, 40, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.pushButton_browse.setFont(font)
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.textbox_api = QtWidgets.QLineEdit(self.frame_2)
        self.textbox_api.setGeometry(QtCore.QRect(24, 80, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.textbox_api.setFont(font)
        self.textbox_api.setObjectName("textbox_api")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(28, 124, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.spinBox_minuts = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox_minuts.setGeometry(QtCore.QRect(130, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.spinBox_minuts.setFont(font)
        self.spinBox_minuts.setMinimum(1)
        self.spinBox_minuts.setMaximum(30)
        self.spinBox_minuts.setProperty("value", 10)
        self.spinBox_minuts.setObjectName("spinBox_minuts")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(225, 124, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(350, 90, 251, 251))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_sent = QtWidgets.QLabel(self.groupBox)
        self.label_sent.setGeometry(QtCore.QRect(20, 30, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_sent.setFont(font)
        self.label_sent.setObjectName("label_sent")
        self.label_badproxy = QtWidgets.QLabel(self.groupBox)
        self.label_badproxy.setGeometry(QtCore.QRect(20, 210, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_badproxy.setFont(font)
        self.label_badproxy.setObjectName("label_badproxy")
        self.label_spm = QtWidgets.QLabel(self.groupBox)
        self.label_spm.setGeometry(QtCore.QRect(20, 90, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_spm.setFont(font)
        self.label_spm.setObjectName("label_spm")
        self.label_timeout = QtWidgets.QLabel(self.groupBox)
        self.label_timeout.setGeometry(QtCore.QRect(20, 180, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_timeout.setFont(font)
        self.label_timeout.setObjectName("label_timeout")
        self.label_unknown = QtWidgets.QLabel(self.groupBox)
        self.label_unknown.setGeometry(QtCore.QRect(20, 60, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_unknown.setFont(font)
        self.label_unknown.setObjectName("label_unknown")
        self.label_error = QtWidgets.QLabel(self.groupBox)
        self.label_error.setGeometry(QtCore.QRect(20, 150, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label_error.setFont(font)
        self.label_error.setObjectName("label_error")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(50, 10, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.logo.setFont(font)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(icon_photo))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(140, 10, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 50, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ad_1 = QtWidgets.QLabel(self.centralwidget)
        self.ad_1.setGeometry(QtCore.QRect(350, 360, 251, 101))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.ad_1.setFont(font)
        self.ad_1.setText("")
        self.ad_1.setPixmap(QtGui.QPixmap(ad_1_photo))
        self.ad_1.setScaledContents(True)
        self.ad_1.setObjectName("ad_1")

        self.ad_2 = QtWidgets.QLabel(self.centralwidget)
        self.ad_2.setGeometry(QtCore.QRect(350, 480, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.ad_2.setFont(font)
        self.ad_2.setText("")
        self.ad_2.setPixmap(QtGui.QPixmap(ad_2_photo))
        self.ad_2.setScaledContents(True)
        self.ad_2.setObjectName("ad_2")

        self.tufaah = QtWidgets.QLabel(self.centralwidget)
        self.tufaah.setGeometry(QtCore.QRect(350, 590, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.tufaah.setFont(font)
        self.tufaah.setAlignment(QtCore.Qt.AlignCenter)
        self.tufaah.setObjectName("tufaah")
        self.tufaah_2 = QtWidgets.QLabel(self.centralwidget)
        self.tufaah_2.setGeometry(QtCore.QRect(550, 10, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.tufaah_2.setFont(font)
        self.tufaah_2.setAlignment(QtCore.Qt.AlignCenter)
        self.tufaah_2.setObjectName("tufaah_2")
        self.label_2.raise_()
        self.label_1.raise_()
        self.pushButton_start.raise_()
        self.textbox_channel.raise_()
        self.spinBox_timeout.raise_()
        self.comboBox_proxytype.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.frame.raise_()
        self.spinBox_threads.raise_()
        self.label_6.raise_()
        self.frame_2.raise_()
        self.groupBox.raise_()
        self.ad_1.raise_()
        self.ad_2.raise_()
        self.tufaah.raise_()
        self.logo.raise_()
        self.tufaah_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        notEnabled = [self.textbox_api, self.spinBox_minuts]
        for ne in notEnabled:
            ne.setEnabled(False)

        self.pushButton_start.clicked.connect(self.start)
        self.pushButton_browse.clicked.connect(self.browse)
        self.radioButton_proxy_1.toggled.connect(self.proxy_select, 1)
        self.radioButton_proxy_2.toggled.connect(self.proxy_select, 2)
        self.radioButton_post_1.toggled.connect(self.post_select, 1)
        self.radioButton_post_2.toggled.connect(self.post_select, 2)

    def task(self, channel, post, proxy_type):
        global counter, sent, unknown, error, bad_proxy, timeout_error
        timeout_value = int(self.spinBox_timeout.value())
        while True:
            counter += 1
            try:
                proxy = proxies_list[counter]
                proxies = {'http': f'{proxy_type}://{proxy}', 'https': f'{proxy_type}://{proxy}'}
                session = requests.session()

                data_response = session.get(f'https://t.me/{channel}/{post}',
                                            params={'embed': '1', 'mode': 'tme'},
                                            headers={'accept-language': 'en-US,en;q=0.9',
                                                     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                                     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
                                                     'referer': f'https://t.me/{channel}/{post}'},
                                            proxies=proxies, timeout=timeout_value).text

                data_view = search('data-view="([^"]+)', data_response).group(1)
                views_response = session.get('https://t.me/v/',
                                             params={'views': str(data_view)},
                                             headers={'accept': '*/*', 'accept-language': 'en-US,en;q=0.9',
                                                      'referer': f'https://t.me/{channel}/{post}?embed=1&mode=tme',
                                                      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
                                                      'x-requested-with': 'XMLHttpRequest'},
                                             proxies=proxies, timeout=timeout_value).status_code
                if views_response == 200: sent += 1
                else: unknown += 1

            except requests.exceptions.Timeout: timeout_error += 1
            except requests.exceptions.ConnectionError: bad_proxy += 1
            except IndexError:
                if is_api: counter = 0
                else: break
            except Exception as ex:
                error += 1
                logs_file.write(f'Error: {ex}\n')


    def start(self):
        global is_api
        if self.radioButton_proxy_2.isChecked():
            is_api = True
            Thread(target=self.api).start()

        is_ranged, post_value = False, ''
        if self.radioButton_post_1.isChecked(): post_value += str(self.textbox_post.text())
        else:
            post_value += str((int(self.spinBox_range_1.value()), int(self.spinBox_range_2.value())+1))
            is_ranged = True

        channel_value = str(self.textbox_channel.text()).replace('@', '')
        threads_value = int(self.spinBox_threads.value())
        proxy_type_value = str(self.comboBox_proxytype.currentText())
        if not channel_value:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Cant find your channel username!")
            msg.setWindowTitle("Not found!")
            msg.exec_()

        else:
            proxy_type = "http"
            if "4" in proxy_type_value: proxy_type = "socks4"
            elif "5" in proxy_type_value: proxy_type = "socks5"

            notEnabled = [self.pushButton_browse, self.radioButton_proxy_1, self.radioButton_proxy_2, self.textbox_api, self.spinBox_minuts,
                          self.comboBox_proxytype, self.spinBox_timeout, self.spinBox_threads,
                          self.pushButton_start, self.textbox_channel, self.textbox_post]
            for ne in notEnabled:
                ne.setEnabled(False)

            Thread(target=self.update).start()
            Thread(target=self.spm_update).start()
            if is_ranged:
                pv1 = post_value.replace(')', '').replace('(', '').replace(' ', '').split(',')
                for i in range(threads_value):
                    for pv in range(int(pv1[0]), int(pv1[1])):
                        thread = Thread(target=self.task, args=(channel_value, pv, proxy_type))
                        thread.start()

            else:
                for i in range(threads_value):
                    thread = Thread(target=self.task, args=(channel_value, post_value, proxy_type))
                    thread.start()

    def browse(self):
        global proxies_list
        file_path = fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Select the proxies file in txt', '',)
        proxies_file = open(rf'{file_path[0]}', 'r')
        proxies_list = proxies_file.read().splitlines()
        proxies_file.close()
        notEnabled = [self.pushButton_browse, self.radioButton_proxy_1, self.radioButton_proxy_2, self.textbox_api, self.spinBox_minuts]
        for ne in notEnabled:
            ne.setEnabled(False)

    def api(self):
        global proxies_list, error
        sleep_time = int(self.spinBox_minuts.value())
        while True:
            try:
                proxies_list = requests.get(str(self.textbox_api.text())).text.splitlines()
                sleep(sleep_time * 60)
            except:
                error += 1

    def update(self):
        global sent, unknown, error, bad_proxy, timeout_error
        while True:
            update_list = [(self.label_sent, f"Sent: {sent}"),
                           (self.label_unknown, f"Unknown: {unknown}"),
                           (self.label_error, f"Errors: {error}"),
                           (self.label_timeout, f"Timeout Erros: {timeout_error}"),
                           (self.label_badproxy, f"Bad Proxies: {bad_proxy}")]
            for ul in update_list:
                ul[0].setText(ul[1])
                ul[0].adjustSize()

            sleep(2)

    def spm_update(self):
        global spm, sent, unknown, error, bad_proxy, timeout_error
        while True:
            try:
                oldchecked = sent + unknown
                sleep(1)
                newchecked = sent + unknown
                spm = (newchecked - oldchecked) * 60
                self.label_spm.setText(f'SPM: {spm}')
                self.label_spm.adjustSize()
            except: pass

    def proxy_select(self, s):
        if s == 1:
            self.pushButton_browse.setEnabled(False)
            self.textbox_api.setEnabled(True)
            self.spinBox_minuts.setEnabled(True)
        else:
            self.textbox_api.setEnabled(False)
            self.spinBox_minuts.setEnabled(False)
            self.pushButton_browse.setEnabled(True)

    def post_select(self, s):
        if s == 1:
            self.textbox_post.setEnabled(False)
            self.spinBox_range_2.setEnabled(True)
            self.spinBox_range_1.setEnabled(True)
        else:
            self.spinBox_range_1.setEnabled(False)
            self.spinBox_range_2.setEnabled(False)
            self.textbox_post.setEnabled(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Telegram views sender | By: @Tufaah"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.textbox_channel.setPlaceholderText(_translate("MainWindow", "Enter Your Channel Username"))
        self.comboBox_proxytype.setItemText(0, _translate("MainWindow", "HTTP/S"))
        self.comboBox_proxytype.setItemText(1, _translate("MainWindow", "SOCKS4"))
        self.comboBox_proxytype.setItemText(2, _translate("MainWindow", "SOCKS5"))
        self.label_7.setText(_translate("MainWindow", "Timeout:"))
        self.label_8.setText(_translate("MainWindow", "Proxies:"))
        self.label_4.setText(_translate("MainWindow", "Range:"))
        self.label_5.setText(_translate("MainWindow", "To:"))
        self.radioButton_post_2.setText(_translate("MainWindow", "Multi Posts"))
        self.radioButton_post_1.setText(_translate("MainWindow", "One Post"))
        self.label_3.setText(_translate("MainWindow", "Send To:"))
        self.textbox_post.setPlaceholderText(_translate("MainWindow", "Post Number"))
        self.label_6.setText(_translate("MainWindow", "Threads:"))
        self.radioButton_proxy_1.setText(_translate("MainWindow", "File"))
        self.radioButton_proxy_2.setText(_translate("MainWindow", "API"))
        self.label_9.setText(_translate("MainWindow", "Proxies From:"))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse "))
        self.textbox_api.setPlaceholderText(_translate("MainWindow", "Api Url"))
        self.label_10.setText(_translate("MainWindow", "Auto update:"))
        self.label_11.setText(_translate("MainWindow", "minutes"))
        self.groupBox.setTitle(_translate("MainWindow", " Stats "))
        self.label_sent.setText(_translate("MainWindow", "Sent: 0"))
        self.label_badproxy.setText(_translate("MainWindow", "Bad Proxies: 0"))
        self.label_spm.setText(_translate("MainWindow", "SPM: 0"))
        self.label_timeout.setText(_translate("MainWindow", "Timeout Erros: 0"))
        self.label_unknown.setText(_translate("MainWindow", "Unknown: 0"))
        self.label_error.setText(_translate("MainWindow", "Errors: 0"))
        self.label_1.setText(_translate("MainWindow", "Telegram views sender"))
        self.label_2.setText(_translate("MainWindow", "Coded By: @Tufaah"))
        self.tufaah.setText(_translate("MainWindow", "https://t.me/Tufaah"))
        self.tufaah_2.setText(_translate("MainWindow", "v1.0"))



app = QtWidgets.QApplication(argv)
app.setStyleSheet(load_stylesheet_pyqt5())
MainWindow = QtWidgets.QMainWindow()
ui = GUI()
ui.setupUi(MainWindow)
MainWindow.show()
exit(app.exec_())
