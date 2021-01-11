from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from pyqtgraph.Qt import QtGui
from PyQt5 import QtGui
from threading import Thread
import time
from LoginWidget import *
from LoginForm import *
from SftpClient import *
import pandas as pd
import sys,os,re


class MainWindow(QtGui.QMainWindow):
    started = pyqtSignal()
    finished = pyqtSignal()
    started_par = pyqtSignal()
    finished_par = pyqtSignal()
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('File SET')
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.login_widget = LoginWidget(self)
        #self.resize(1314, 916)

        ###########################################################################################
        #
        #              Buttons and word design GUI
        #
        self.login_widget.label.setText("<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">IP:</span></p></body></html>")
        self.login_widget.label_2.setText("<html><head/><body><p><span style=\" font-size:20pt;\">Device Type:</span></p></body></html>")
        self.login_widget.Connect.setText("Connect")
        self.login_widget.CurrentSetting.setText("Current Setting")
        self.login_widget.ChangeSetting.setText("Change Setting")
        self.login_widget.label_3.setText("<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">AE:</span></p></body></html>")
        self.login_widget.label_4.setText("<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">ITS:</span></p></body></html>")
        self.login_widget.MacIPtextEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n""</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n""<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.login_widget.label_5.setText("<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">AE:</span></p></body></html>")
        self.login_widget.label_6.setText("<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">ITS:</span></p></body></html>")
        self.login_widget.label_7.setText("<html><head/><body><p><span style=\" font-size:10pt;\">File Save Directory:</span></p></body></html>")
        self.login_widget.label_8.setText("<html><head/><body><p><span style=\" font-size:10pt;\">File Type:</span></p></body></html>")
        self.login_widget.label_9.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Sampling Rate :</span></p></body></html>")
        self.login_widget.label_10.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">F - T :</span></p></body></html>")
        self.login_widget.label_11.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">T-P :</span></p></body></html>")
        self.login_widget.label_12.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">File server ID :</span></p></body></html>")
        self.login_widget.label_13.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">File server PW :</span></p></body></html>")
        self.login_widget.label_14.setText("<html><head/><body><p><span style=\" font-size:10pt;\">File Save Directory:</span></p></body></html>")
        self.login_widget.label_15.setText("<html><head/><body><p><span style=\" font-size:10pt;\">File Save Directory:</span></p></body></html>")
        self.login_widget.label_16.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Sampling Rate </span><span style=\" font-size:10pt;\">:</span></p></body></html>")
        self.login_widget.label_17.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">F - T :</span></p></body></html>")
        self.login_widget.label_18.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">T-P :</span></p></body></html>")
        self.login_widget.label_19.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">D-A-M:</span></p></body></html>")
        self.login_widget.label_20.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">S_Type:</span></p></body></html>")
        self.login_widget.label_21.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">S_Sys:</span></p></body></html>")
        self.login_widget.label_22.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">D-A-M:</span></p></body></html>")
        self.login_widget.label_23.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">S_Type:</span></p></body></html>")
        self.login_widget.label_24.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">T_Sys:</span></p></body></html>")
        self.login_widget.label_25.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">File server PW :</span></p></body></html>")
        self.login_widget.FileSaveIDlabel.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">File server ID :</span></p></body></html>")
        self.login_widget.label_26.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Sensor Num  :</span></p></body></html>")
        self.login_widget.label_27.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Sensor Num  :</span></p></body></html>")
        self.login_widget.label_28.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Mac IP :</span></p></body></html>")
        self.login_widget.label_29.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Sensitivity:</span></p></body></html>")
        self.login_widget.label_30.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Ext factor:</span></p></body></html>")
        self.login_widget.label_31.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Range:</span></p></body></html>")
        self.login_widget.label_32.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">G_factor:</span></p></body></html>")
        self.login_widget.label_33.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Capacity:</span></p></body></html>")
        self.login_widget.label_34.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">offset:</span></p></body></html>")
        self.login_widget.label_35.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">exVolt:</span></p></body></html>")
        self.login_widget.label_36.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Voltage:</span></p></body></html>")
        self.login_widget.label_37.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Ext factor:</span></p></body></html>")
        self.login_widget.label_38.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">exVolt:</span></p></body></html>")
        self.login_widget.label_39.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Sensitivity:</span></p></body></html>")
        self.login_widget.label_40.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Mac IP :</span></p></body></html>")
        self.login_widget.label_41.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Voltage:</span></p></body></html>")
        self.login_widget.label_42.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Capacity:</span></p></body></html>")
        self.login_widget.label_43.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">offset:</span></p></body></html>")
        self.login_widget.label_44.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">G_factor:</span></p></body></html>")
        self.login_widget.label_45.setText("<html><head/><body><p><span style=\" font-family:\'맑은 고딕\'; font-size:10pt; color:#000000;\">Range:</span></p></body></html>")
        self.login_widget.ApplyBtn.setText( "Apply")
        self.login_widget.DeleteBtn.setText("Delete")
        self.login_widget.AddBtn.setText("Add")

        ###########################################################################################
        #
        #               QMessageBox action function
        #
        self._message_box = QMessageBox()
        self._message_box.setStyleSheet("background-color: #d0f5b9;");
        self._message_box.setText(str('Change Setting get Variable is done...!'))
        self._message_box.setStandardButtons(QMessageBox.NoButton)
        self.started.connect(self._message_box.show)
        self.finished.connect(self._message_box.accept)

        self._message_par = QMessageBox()
        self._message_par.setStyleSheet("background-color: #63f8f2;");
        self._message_par.setText(str('Parameter has been added to the files...!'))
        self._message_par.setStandardButtons(QMessageBox.NoButton)
        self.started_par.connect(self._message_par.show)
        self.finished_par.connect(self._message_par.accept)
        ###########################################################################################
        #
        #               Buttons action function
        #
        self.login_widget.Connect.clicked.connect(self.convertclick)

        # Set value of counter
        self.counterL = 0
        self.update_counterL()

        self.counterR = 0
        self.update_counterR()

        # Bind Current setting
        self.login_widget.pushButtonLeft.clicked.connect(self.incL)
        self.login_widget.pushButtonRight.clicked.connect(self.decL)
        self.login_widget.CurrentSetting.clicked.connect(self.CurrentSet)

        # Bind Change settinge
        self.login_widget.pushButtonSetLeft.clicked.connect(self.incR)
        self.login_widget.pushButtonSetRight.clicked.connect(self.decR)
        self.login_widget.ChangeSetting.clicked.connect(self.ChangeSet)
        self.login_widget.ApplyBtn.clicked.connect(self.ApplySet)
        self.login_widget.AddBtn.clicked.connect(self.Addset)
        self.login_widget.DeleteBtn.clicked.connect(self.DeleteSet)
        self.port = 22
        self.resize(1314, 916)
        self.central_widget.addWidget(self.login_widget)


    @pyqtSlot()
    def convertclick(self):
        self.ipaddr = self.login_widget.lineEdit.text()
        if self.login_widget.comboBox.currentText() == "S-Cube":
            self.main_config = "/home/pi/SCube2/conf/main_config.txt"
            self.analysis_config = "/home/pi/SCube2/conf/analysis_config.txt"
            self.sensor_config = "/home/pi/SCube2/conf/sensor_config.txt"
            self.procMon = "/home/pi/SCube2/procMon.sh"
            self.managment = "/home/pi/SCube2/file_management.sh"
            self.protocol_config = "/home/pi/SCube2/conf/protocol_config.txt"

        self.login_dialog = LoginForm(self, self.ipaddr)
        self.main_config_local_path = 'files/main_config.txt'
        self.analysis_local_path = 'files/analysis_config.txt'
        self.sensor_config_local_path = 'files/sensor_config.txt'
        self.procMon_local_path = 'files/procMon.sh'
        self.managment_local_path = 'files/file_management.sh'
        self.protocol_config_path  = 'files/protocol_config.txt'

        while self.login_dialog.boolean:
            try:
                self.client = SftpClient(self.ipaddr, self.port, self.login_dialog.user, self.login_dialog.password)
                self.client.download(self.main_config, self.main_config_local_path)
                self.client.download(self.analysis_config, self.analysis_local_path)
                self.client.download(self.sensor_config, self.sensor_config_local_path)
                self.client.download(self.procMon,  self.procMon_local_path)
                self.client.download(self.managment, self.managment_local_path)
                self.client.download(self.protocol_config, self.protocol_config_path)

                input_data = pd.read_csv(self.main_config_local_path, header=None);
                analysis_data = pd.read_csv(self.analysis_local_path, header=None);
                file_manage_data = pd.read_csv(self.managment_local_path, header=None);
                sensor_data =  pd.read_csv(self.sensor_config_local_path, sep='\n', header =None);
                procmMon_data = pd.read_csv(self.procMon_local_path, sep='\n', header=None);
                protocol_config_data = pd.read_csv(self.protocol_config_path, sep='\n', header=None);

                ip_show = str(input_data[0:1]).split('=', 1)[1]
                AE_show = str(input_data[3:4]).split('=', 1)[1]
                FSDir_show = str(input_data[5:6]).split('=', 1)[1]
                Ftype_show = str(input_data[6:7]).split('=', 1)[1]
                analysis_show = str(analysis_data[1:2]).split('=', 1)[1]

                S_Type_show = str(sensor_data[0:1]).split(',', 1)[1]
                FT_show = str(sensor_data[0:1]).split('=', 1)[1].split(',')[0]
                Senty_show = str(sensor_data[2:3]).split('=', 1)[1].split(',')[0]
                cap_show = str(sensor_data[3:4]).split('=', 1)[1].split(',')[0]
                ext_fac_show = str(sensor_data[4:5]).split('=', 1)[1].split(',')[0]
                offset_show = str(sensor_data[5:6]).split('=', 1)[1].split(',')[0]
                range_show = str(sensor_data[6:7]).split('=', 1)[1].split(',')[0]
                exVolt_show = str(sensor_data[7:8]).split('=', 1)[1].split(',')[0]
                Gfactor_show = str(sensor_data[8:9]).split('=', 1)[1].split(',')[0]
                vol_show = str(sensor_data[9:10]).split('=', 1)[1].split(',')[0]
                #ctemp_1_show = str(sensor_data[10:11]).split('=', 1)[1].split(',')[0]
                #ctemp_2_show = str(sensor_data[11:12]).split('=', 1)[1].split(',')[0]

                FTP_USER = str(file_manage_data[17:18]).split('=', 1)[1]
                FTP_PASS = str(file_manage_data[18:19]).split('=', 1)[1]
                T_SYS_show = str(procmMon_data[7:8]).split('-', 1)[1].split(' ')[0]
                D_A_M_show = str(protocol_config_data[0:1]).split('=', 1)[1]
                F_T_show = str(protocol_config_data[1:2]).split('=', 1)[1]

                self.login_widget.ITSlineEdit.setText(ip_show)
                self.login_widget.AElineEdit.setText(AE_show)
                self.login_widget.AElineSettingEdit.setText(str(AE_show))
                self.login_widget.FileSaveDirTextEdit.setText(FSDir_show)
                self.login_widget.FileSaveDirtextEdit.setText(FSDir_show)
                if int(Ftype_show) == 0:
                    self.login_widget.textEdit_2.setText("NONE")
                elif int(Ftype_show) == 1:
                    self.login_widget.textEdit_2.setText("ASCII")
                elif int(Ftype_show) == 2:
                    self.login_widget.textEdit_2.setText("BIN")

                if int(S_Type_show) == 0:
                    self.login_widget.textEdit_6.setText("ACC-X")
                elif int(S_Type_show) == 1:
                    self.login_widget.textEdit_6.setText("ACC-Y")
                elif int(S_Type_show) == 2:
                    self.login_widget.textEdit_6.setText("ACC-Z")
                elif int(S_Type_show) == 3:
                    self.login_widget.textEdit_6.setText("ACC-3A")
                elif int(S_Type_show) == 4:
                    self.login_widget.textEdit_6.setText("Strain")
                elif int(S_Type_show) == 5:
                    self.login_widget.textEdit_6.setText("DISP")
                elif int(S_Type_show) == 6:
                    self.login_widget.textEdit_6.setText("LOAD")
                elif int(S_Type_show) == 7:
                    self.login_widget.textEdit_6.setText("TILT")

                if T_SYS_show == 's':
                    self.login_widget.textEdit_8.setText("NTP")
                elif T_SYS_show == 't':
                    self.login_widget.textEdit_8.setText("GPS")

                if int(D_A_M_show) == 1:
                    self.login_widget.textEdit_5.setText("MQTT")
                elif int(D_A_M_show) == 2:
                    self.login_widget.textEdit_5.setText("ITS")
                elif int(D_A_M_show) == 3:
                    self.login_widget.textEdit_5.setText("MQTT + ITS")
                elif int(D_A_M_show) == 4:
                    self.login_widget.textEdit_5.setText("KT")
                elif int(D_A_M_show) == 5:
                    self.login_widget.textEdit_5.setText("KT + MQTT")
                elif int(D_A_M_show) == 6:
                    self.login_widget.textEdit_5.setText("KT + ITS")

                self.login_widget.SamRateTextEdit.setText(FT_show)
                self.login_widget.TPtextEdit.setText(analysis_show)
                self.login_widget.FileServerIDtextEdit.setText(FTP_USER.translate({ord('"'): None}))
                self.login_widget.FileServerPWTextEdit.setText(FTP_PASS.translate({ord('"'): None}))

                self.login_widget.FileSaveIDlsettingsTxtEdit.setText(FTP_USER.translate({ord('"'): None}))
                self.login_widget.FileServerPWsettingsTextEdit.setText(FTP_PASS.translate({ord('"'): None}))

                self.login_widget.SensitytextEdit.setText(Senty_show)
                self.login_widget.CaptextEdit.setText(cap_show)
                self.login_widget.ExtFactortextEdit.setText(ext_fac_show)
                self.login_widget.RangetextEdit.setText(range_show)
                self.login_widget.GFactortextEdit.setText(Gfactor_show)
                self.login_widget.OffsettextEdit.setText(offset_show)
                self.login_widget.exVolttextEdit.setText(exVolt_show)
                self.login_widget.VoltagetextEdit.setText(vol_show)

                self.login_widget.SensityChangSettextEdit.setText(Senty_show)
                self.login_widget.CapChangSettextEdit.setText(cap_show)
                self.login_widget.ExtFactorChangSettextEdit.setText(ext_fac_show)
                self.login_widget.RangeChangSettextEdit.setText(range_show)
                self.login_widget.GFactorChanSettextEdit.setText(Gfactor_show)
                self.login_widget.OffsetChanSettextEdit.setText(offset_show)
                self.login_widget.exVoltChanSettextEdit.setText(exVolt_show)
                self.login_widget.VoltageChanSettextEdit.setText(vol_show)
                self.login_widget.FTtextEdit.setText(F_T_show)

                #self.login_widget.MacIPtextEdit.setText()
                #self.login_widget.MacIPChanSettextEdit.setText()

                self.login_widget.sersorNumtextEdit.setText("1")
                self.login_widget.senNumSetgsTextEdit.setText("1")
                self.login_widget.Connect.setStyleSheet('QPushButton {background-color: #b3ffb3; color: rgb(102, 140, 255);}')
                self.login_widget.Connect.setText('Connected')

            #here is the ftp conncetion set
            except:
                self.login_widget.Connect.setText('Disconnect')
                QMessageBox.about(self, self.ipaddr, "device connection is error")
            print(self.login_dialog.user)
            print(self.login_dialog.password)
            break

        self.client.close()

    def update_counterL(self):
        self.login_widget.textEditCurSet.setText(str(self.counterL))

    def incL(self):
        self.counterL += 1
        self.update_counterL()

    def decL(self):
        self.counterL -= 1
        self.update_counterL()

    def update_counterR(self):
        self.login_widget.textEditSetChan.setText(str(self.counterR))

    def incR(self):
        self.counterR += 1
        self.update_counterR()

    def decR(self):
        self.counterR -= 1
        self.update_counterR()

    def reset(self):
        self.counterL = 0
        self.update_counterL()

    def CurrentSet(self):
        self.login_widget.sersorNumtextEdit.setText(str(self.counterL))

    def ChangeSet(self):
        self.login_widget.senNumSetgsTextEdit.setText(str(self.counterR))
        #print(Lineedit)
        #print(str(self.login_widget.FileSaveDirtextEdit.toPlainText()))

        ############################# ITS change set ##################################
        if str(self.login_widget.ITScomboBo.currentText()) == 'ITS1':
            self.var_ITS = "210.105.85.7"
        elif str(self.login_widget.ITScomboBo.currentText()) == 'ITS2':
            self.var_ITS = "210.105.85.20"
        elif str(self.login_widget.ITScomboBo.currentText()) == 'ITS3':
            self.var_ITS = "210.105.85.3"

        ############################# FileSaveDirkombo change set ################################
        if str(self.login_widget.FileSaveDirkombo.currentText()) == 'BIN':
            self.var_FileType = "2"
        elif str(self.login_widget.FileSaveDirkombo.currentText()) == 'csv':
            self.var_FileType = "1"
        elif str(self.login_widget.FileSaveDirkombo.currentText()) == '저장안함':
            self.var_FileType = "0"

        ############################# D-A-M change set ################################
        if str(self.login_widget.DAMkombo.currentText()) == 'MQTT':
            self.var_D_A_M = "1"
        elif str(self.login_widget.DAMkombo.currentText()) == 'ITS':
            self.var_D_A_M = "2"
        elif str(self.login_widget.DAMkombo.currentText()) == 'MQTT+ITS':
            self.var_D_A_M = "3"
        elif str(self.login_widget.DAMkombo.currentText()) == 'KT':
            self.var_D_A_M = "4"
        elif str(self.login_widget.DAMkombo.currentText()) == 'KT+MQTT':
            self.var_D_A_M = "5"
        elif str(self.login_widget.DAMkombo.currentText()) == 'KT+ITS':
            self.var_D_A_M = "6"

        ############################# S-Type change set ##################################
        if str(self.login_widget.S_Typekombo.currentText()) == 'ACC-X':
            self.var_S_Type = "0"
        elif str(self.login_widget.S_Typekombo.currentText()) == 'ACC-Y':
            self.var_S_Type = "1"
        elif str(self.login_widget.S_Typekombo.currentText()) == 'ACC-Z':
            self.var_S_Type = "2"
        elif str(self.login_widget.S_Typekombo.currentText()) == 'ACC-3A':
            self.var_S_Type = "3"
        elif str(self.login_widget.S_Typekombo.currentText()) == 'Strain':
            self.var_S_Type = "4"
        elif str(self.login_widget.S_Typekombo.currentText()) == 'DISP':
            self.var_S_Type = "5"
        elif str(self.login_widget.S_Typekombo.currentText()) == 'LOAD':
            self.var_S_Type = "6"
        elif str(self.login_widget.S_Typekombo.currentText()) == 'TILT':
            self.var_S_Type = "7"

        ############################# T_Syskombo change set ##################################
        if str(self.login_widget.T_Syskombo.currentText()) == 'NTP':
            self.var_T_Sys = "s"
        elif str(self.login_widget.T_Syskombo.currentText()) == 'GPS':
            self.var_T_Sys = "t"

        ############################# T-P change set ##################################
        if str(self.login_widget.TPkombo.currentText()) == 'Periodic':
            self.var_T_P = "2"
        elif str(self.login_widget.TPkombo.currentText()) == 'Event':
            self.var_T_P = "1"

        print(self.var_ITS)
        print(self.var_FileType)
        thread = Thread(target=self.dowork, daemon=True)
        thread.start()

    def dowork(self):
        delay = 1.5
        self.started.emit()
        while delay:
            sys.stdout.write('Geting variable...\n')
            time.sleep(0.5)  # do some time-consuming stuff...
            delay -= 0.5
        self.finished.emit()

    @pyqtSlot()
    def Addset(self):
        '''
        main_config_local_path = 'files/main_config.txt'
        procMon_local_path = 'files/procMon.sh'
        managment_local_path = 'files/file_management.sh'
        analysis_local_path = 'files/analysis_config.txt'
        protocol_config_path = 'files/protocol_config.txt'
        sensor_config_local_path = 'files/sensor_config.txt'
        '''
        try:
            with open(self.main_config_local_path, 'r') as main_config_file,\
                    open(self.procMon_local_path, 'r') as procMon_local_file,\
                    open(self.managment_local_path, 'r') as managment_local_file,\
                    open(self.analysis_local_path, 'r') as analysis_local_file,\
                    open(self.protocol_config_path, 'r') as protocol_config_file,\
                    open(self.sensor_config_local_path, 'r') as sensor_config_local_file:

                main_config_filedata = main_config_file.read()
                procMon_local_filedata = procMon_local_file.read()
                file_management_filedata = managment_local_file.read()
                analysis_local_filedata = analysis_local_file.read()
                protocol_config_filedata = protocol_config_file.read()
                sensor_config_local_filedata = sensor_config_local_file.read()

            main_config_filedata = re.sub('(?m)^PF-IP = .*', 'PF-IP = '+self.var_ITS, main_config_filedata)
            main_config_filedata = re.sub('(?m)^D-ID = .*', 'D-ID = '+self.login_widget.AElineSettingEdit.text().strip(), main_config_filedata)
            main_config_filedata = re.sub('(?m)^FileSaveDirectory = .*', 'FileSaveDirectory = ' + self.login_widget.FileSaveDirtextEdit.toPlainText().strip(), main_config_filedata)
            main_config_filedata = re.sub('(?m)^Filetype = .*', 'Filetype = ' + self.var_FileType, main_config_filedata)

            procMon_local_filedata = re.sub('(?m)^./ITSSCube2_206 .*','./ITSSCube2_206 -'+self.var_T_Sys+' &',procMon_local_filedata)

            file_management_filedata =  re.sub('(?m)^FTP_USER=.*','FTP_USER="'+self.login_widget.FileSaveIDlsettingsTxtEdit.toPlainText()+'"',file_management_filedata)
            file_management_filedata = re.sub('(?m)^FTP_PASS=.*', 'FTP_PASS="' +self.login_widget.FileServerPWsettingsTextEdit.toPlainText()+ '"', file_management_filedata)

            analysis_local_filedata = re.sub('(?m)^T-P = .*', 'T-P = '+self.var_T_P, analysis_local_filedata)

            protocol_config_filedata = re.sub('(?m)^D-A-M = .*', 'D-A-M = '+self.var_D_A_M, protocol_config_filedata)
            protocol_config_filedata = re.sub('(?m)^F-T = .*', 'F-T = '+self.login_widget.FTkombo.currentText(), protocol_config_filedata)

            sensor_config_local_filedata = re.sub('(?m)^ycommand = .*', 'ycommand = ' + self.login_widget.SampRatekombo.currentText() + ',' + self.var_S_Type, sensor_config_local_filedata)
            sensor_config_local_filedata = re.sub('(?m)^sensitivity = .*', 'sensitivity = ' + self.login_widget.SensityChangSettextEdit.toPlainText().strip() + ',' + self.login_widget.SensityChangSettextEdit.toPlainText().strip() + ',' + self.login_widget.SensityChangSettextEdit.toPlainText().strip(), sensor_config_local_filedata)
            sensor_config_local_filedata = re.sub('(?m)^capacity = .*', 'capacity = ' + self.login_widget.CapChangSettextEdit.toPlainText().strip() + ',' +  self.login_widget.CapChangSettextEdit.toPlainText().strip() + ',' +  self.login_widget.CapChangSettextEdit.toPlainText().strip(), sensor_config_local_filedata)
            sensor_config_local_filedata = re.sub('(?m)^ext_factor = .*', 'ext_factor = ' + self.login_widget.ExtFactorChangSettextEdit.toPlainText().strip() + ',' + self.login_widget.ExtFactorChangSettextEdit.toPlainText().strip() + ',' + self.login_widget.ExtFactorChangSettextEdit.toPlainText().strip(), sensor_config_local_filedata)
            sensor_config_local_filedata = re.sub('(?m)^offset = .*', 'offset = ' + self.login_widget.OffsetChanSettextEdit.toPlainText().strip() + ',' + self.login_widget.OffsetChanSettextEdit.toPlainText().strip() + ',' + self.login_widget.OffsetChanSettextEdit.toPlainText().strip(), sensor_config_local_filedata)
            sensor_config_local_filedata = re.sub('(?m)^range = .*', 'range = ' + self.login_widget.RangeChangSettextEdit.toPlainText().strip() + ',' + self.login_widget.RangeChangSettextEdit.toPlainText().strip() + ',' + self.login_widget.RangeChangSettextEdit.toPlainText().strip(), sensor_config_local_filedata)
            sensor_config_local_filedata = re.sub('(?m)^exVolt = .*', 'exVolt = ' + self.login_widget.exVoltChanSettextEdit.toPlainText().strip() + ',' + self.login_widget.exVoltChanSettextEdit.toPlainText().strip() + ',' + self.login_widget.exVoltChanSettextEdit.toPlainText().strip(), sensor_config_local_filedata)
            sensor_config_local_filedata = re.sub('(?m)^g_factor = .*', 'g_factor = ' + self.login_widget.GFactorChanSettextEdit.toPlainText().strip() + ',' + self.login_widget.GFactorChanSettextEdit.toPlainText().strip() + ',' + self.login_widget.GFactorChanSettextEdit.toPlainText().strip(), sensor_config_local_filedata)
            sensor_config_local_filedata = re.sub('(?m)^voltage = .*', 'voltage = ' + self.login_widget.VoltageChanSettextEdit.toPlainText().strip() + ',' +  self.login_widget.VoltageChanSettextEdit.toPlainText().strip() + ',' +  self.login_widget.VoltageChanSettextEdit.toPlainText().strip(), sensor_config_local_filedata)

            print(main_config_filedata)
            print("_____________________________________")
            print(procMon_local_filedata)
            print("_____________________________________")
            print(sensor_config_local_filedata)
            with open(self.main_config_local_path, "w") as main_config_wfile,\
                    open(self.procMon_local_path, "w") as procMon_local_wfiledata,\
                    open(self.managment_local_path, "w") as managment_local_wfiledata,\
                    open(self.analysis_local_path, "w") as analysis_local_wfiledata,\
                    open(self.protocol_config_path, "w") as protocol_config_wfiledata,\
                    open(self.sensor_config_local_path, "w") as sensor_config_local_wfiledata:

                main_config_wfile.write(main_config_filedata)
                procMon_local_wfiledata.write(procMon_local_filedata)
                managment_local_wfiledata.write(file_management_filedata)
                analysis_local_wfiledata.write(analysis_local_filedata)
                protocol_config_wfiledata.write(protocol_config_filedata)
                sensor_config_local_wfiledata.write(sensor_config_local_filedata)
                thread_par = Thread(target=self.dowork_par, daemon=True)
                thread_par.start()
        except:
            QMessageBox.about(self, "주의", "Click the button Change Setting")

    def dowork_par(self):
        delay = 1.5
        self.started_par.emit()
        while delay:
            #sys.stdout.write('Adding variable......\n')
            time.sleep(0.5)  # do some time-consuming stuff...
            delay -= 0.5
        self.finished_par.emit()


    @pyqtSlot()
    def ApplySet(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("IP : "+ self.ipaddr+" 주소로 장치 구성을 변경 하시겠습니까?")
        msgBox.setWindowTitle("주의")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.buttonClicked.connect(msgButtonClick)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            clApply = SftpClient(self.ipaddr, self.port, self.login_dialog.user, self.login_dialog.password)
            clApply.upload(self.main_config_local_path, self.main_config)
            clApply.upload(self.analysis_local_path, self.analysis_config)
            clApply.upload(self.sensor_config_local_path, self.sensor_config)
            clApply.upload(self.procMon_local_path, self.procMon)
            clApply.upload(self.managment_local_path, self.managment)
            clApply.upload(self.protocol_config_path, self.protocol_config)
            clApply.close()

    def DeleteSet(self):

        QMessageBox.about(self, "Delete" , "device inforation is deleted!")

def msgButtonClick(i):
    print("operation is:", i.text())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())