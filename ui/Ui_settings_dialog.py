# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Python\Projects\YuQueBackup\ui\settings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(696, 331)
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_token_2 = QtWidgets.QLabel(SettingsDialog)
        self.label_token_2.setObjectName("label_token_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_token_2)
        self.edit_token = QtWidgets.QLineEdit(SettingsDialog)
        self.edit_token.setObjectName("edit_token")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_token)
        self.label_agent = QtWidgets.QLabel(SettingsDialog)
        self.label_agent.setObjectName("label_agent")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_agent)
        self.edit_agent = QtWidgets.QLineEdit(SettingsDialog)
        self.edit_agent.setObjectName("edit_agent")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edit_agent)
        self.Label = QtWidgets.QLabel(SettingsDialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.cb_download_pic = QtWidgets.QCheckBox(SettingsDialog)
        self.cb_download_pic.setObjectName("cb_download_pic")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cb_download_pic)
        self.verticalLayout.addLayout(self.formLayout)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(SettingsDialog)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(SettingsDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "语雀账户配置"))
        self.label_token_2.setText(_translate("SettingsDialog", "ACCESS_TOKEN："))
        self.edit_token.setPlaceholderText(_translate("SettingsDialog", "必填"))
        self.label_agent.setText(_translate("SettingsDialog", "USER_AGENT："))
        self.edit_agent.setPlaceholderText(_translate("SettingsDialog", "必填"))
        self.Label.setText(_translate("SettingsDialog", "同时下载图片："))
        self.plainTextEdit.setPlainText(_translate("SettingsDialog", "详细API教程及配置参见 https://www.yuque.com/yuque/developer\n"
"\n"
"- ACCESS_TOKEN： https://www.yuque.com/settings/tokens \n"
"点右上角新建Token，勾选所有【读取】开头的授权，然后点击【查看详情】\n"
"\n"
"- USER_AGENT：即用户名，例如icheima\n"
"配置的 USER_AGENT 可通过如下格式https://www.yuque.com/icheima访问花园主页，进行验证"))
