# -*- coding: utf-8 -*-

"""
Fichier contenant les fonctions utiles à la gui
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from mainFuncs import *
import os
import time

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(708, 533)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 691, 511))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabView = QtWidgets.QTabWidget(self.verticalLayoutWidget_2)
        self.tabView.setEnabled(True)
        self.tabView.setObjectName("tabView")
        self.searchTab = QtWidgets.QWidget()
        self.searchTab.setObjectName("searchTab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.searchTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 651, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.folderListWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.folderListWidget.setEnabled(True)
        self.folderListWidget.setObjectName("folderListWidget")
        self.verticalLayout.addWidget(self.folderListWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.recursiveBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.recursiveBox.setObjectName("recursiveBox")
        self.horizontalLayout_2.addWidget(self.recursiveBox)
        self.selectFolderBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.selectFolderBtn.setObjectName("selectFolderBtn")
        self.horizontalLayout_2.addWidget(self.selectFolderBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.advFiltersGroupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.advFiltersGroupBox.setEnabled(True)
        self.advFiltersGroupBox.setCheckable(True)
        self.advFiltersGroupBox.setChecked(False)
        self.advFiltersGroupBox.setObjectName("advFiltersGroupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.advFiltersGroupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sizeFilterBox = QtWidgets.QCheckBox(self.advFiltersGroupBox)
        self.sizeFilterBox.setText("")
        self.sizeFilterBox.setObjectName("sizeFilterBox")
        self.horizontalLayout_7.addWidget(self.sizeFilterBox)
        self.filesizeLayout = QtWidgets.QWidget(self.advFiltersGroupBox)
        self.filesizeLayout.setEnabled(False)
        self.filesizeLayout.setObjectName("filesizeLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.filesizeLayout)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.filesizeLayout)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.sizeOverRadio = QtWidgets.QRadioButton(self.filesizeLayout)
        self.sizeOverRadio.setObjectName("sizeOverRadio")
        self.horizontalLayout_9.addWidget(self.sizeOverRadio)
        self.sizeUnderRadio = QtWidgets.QRadioButton(self.filesizeLayout)
        self.sizeUnderRadio.setChecked(True)
        self.sizeUnderRadio.setObjectName("sizeUnderRadio")
        self.horizontalLayout_9.addWidget(self.sizeUnderRadio)
        self.fileSizeTextEdit = QtWidgets.QLineEdit(self.filesizeLayout)
        self.fileSizeTextEdit.setObjectName("fileSizeTextEdit")
        self.horizontalLayout_9.addWidget(self.fileSizeTextEdit)
        self.spinBox = QtWidgets.QSpinBox(self.filesizeLayout)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_9.addWidget(self.spinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.horizontalLayout_7.addWidget(self.filesizeLayout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.modifFilterBox = QtWidgets.QCheckBox(self.advFiltersGroupBox)
        self.modifFilterBox.setText("")
        self.modifFilterBox.setObjectName("modifFilterBox")
        self.horizontalLayout_6.addWidget(self.modifFilterBox)
        self.modifdateLayout = QtWidgets.QWidget(self.advFiltersGroupBox)
        self.modifdateLayout.setEnabled(False)
        self.modifdateLayout.setObjectName("modifdateLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.modifdateLayout)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.modifdateLayout)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.modifAfterRadio = QtWidgets.QRadioButton(self.modifdateLayout)
        self.modifAfterRadio.setObjectName("modifAfterRadio")
        self.horizontalLayout_8.addWidget(self.modifAfterRadio)
        self.modifBeforeRadio = QtWidgets.QRadioButton(self.modifdateLayout)
        self.modifBeforeRadio.setChecked(True)
        self.modifBeforeRadio.setObjectName("modifBeforeRadio")
        self.horizontalLayout_8.addWidget(self.modifBeforeRadio)
        self.modifTimePicker = QtWidgets.QDateTimeEdit(self.modifdateLayout)
        self.modifTimePicker.setObjectName("modifTimePicker")
        self.horizontalLayout_8.addWidget(self.modifTimePicker)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.horizontalLayout_6.addWidget(self.modifdateLayout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.extFilterBox = QtWidgets.QCheckBox(self.advFiltersGroupBox)
        self.extFilterBox.setText("")
        self.extFilterBox.setObjectName("extFilterBox")
        self.horizontalLayout_3.addWidget(self.extFilterBox)
        self.extLayout = QtWidgets.QWidget(self.advFiltersGroupBox)
        self.extLayout.setEnabled(False)
        self.extLayout.setObjectName("extLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.extLayout)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.extLayout)
        self.label_2.setEnabled(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.excludeExtRadio = QtWidgets.QRadioButton(self.extLayout)
        self.excludeExtRadio.setChecked(True)
        self.excludeExtRadio.setObjectName("excludeExtRadio")
        self.horizontalLayout_5.addWidget(self.excludeExtRadio)
        self.includeExtRadio = QtWidgets.QRadioButton(self.extLayout)
        self.includeExtRadio.setObjectName("includeExtRadio")
        self.horizontalLayout_5.addWidget(self.includeExtRadio)
        self.extInput = QtWidgets.QLineEdit(self.extLayout)
        self.extInput.setEnabled(False)
        self.extInput.setInputMask("")
        self.extInput.setText("")
        self.extInput.setObjectName("extInput")
        self.horizontalLayout_5.addWidget(self.extInput)
        self.horizontalLayout_3.addWidget(self.extLayout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.advFiltersGroupBox)
        self.searchBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.searchBtn.setObjectName("searchBtn")
        self.verticalLayout.addWidget(self.searchBtn)
        self.tabView.addTab(self.searchTab, "")
        self.duplicateTab = QtWidgets.QWidget()
        self.duplicateTab.setEnabled(False)
        self.duplicateTab.setObjectName("duplicateTab")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.duplicateTab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 661, 421))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.duplicateListWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.duplicateListWidget.setObjectName("duplicateListWidget")
        self.verticalLayout_4.addWidget(self.duplicateListWidget)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.folderOrderListWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.folderOrderListWidget.setObjectName("folderOrderListWidget")
        self.verticalLayout_4.addWidget(self.folderOrderListWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rankDelBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.rankDelBtn.setCheckable(False)
        self.rankDelBtn.setObjectName("rankDelBtn")
        self.horizontalLayout_4.addWidget(self.rankDelBtn)
        self.rankUpBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.rankUpBtn.setObjectName("rankUpBtn")
        self.horizontalLayout_4.addWidget(self.rankUpBtn)
        self.rankDownBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.rankDownBtn.setObjectName("rankDownBtn")
        self.horizontalLayout_4.addWidget(self.rankDownBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.updFolderOrderBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.updFolderOrderBtn.setObjectName("updFolderOrderBtn")
        self.horizontalLayout_4.addWidget(self.updFolderOrderBtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.cleanBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.cleanBtn.setObjectName("cleanBtn")
        self.verticalLayout_4.addWidget(self.cleanBtn)
        self.tabView.addTab(self.duplicateTab, "")
        self.verticalLayout_2.addWidget(self.tabView)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)

        self.folders = []
        self.folderOrderList = []
        self.dupFiles = []
        self.cleanNeedConfirm = False

        # Pour gérer la hauteur de la advFilterGroupBox
        self.advFilterExpandedHeight = self.advFiltersGroupBox.maximumHeight()
        self.advFilterCollapsedHeight = 18
        self.advFiltersGroupBox.setMaximumHeight(self.advFilterCollapsedHeight)

        self.retranslateUi(Dialog)
        self.tabView.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TriTout v0.1"))
        self.recursiveBox.setText(_translate("Dialog", "Recursive search : Include subfolders"))
        self.selectFolderBtn.setText(_translate("Dialog", "Select folders"))
        self.advFiltersGroupBox.setTitle(_translate("Dialog", "Advanced filters (check to expand)"))
        self.label_6.setText(_translate("Dialog", "Include files with size"))
        self.sizeOverRadio.setText(_translate("Dialog", "Over"))
        self.sizeUnderRadio.setText(_translate("Dialog", "Under"))
        self.label_5.setText(_translate("Dialog", "Include files modified "))
        self.modifAfterRadio.setText(_translate("Dialog", "Before"))
        self.modifBeforeRadio.setText(_translate("Dialog", "After"))
        self.label_2.setText(_translate("Dialog", "Extension list (exemple : jpg, png) :"))
        self.excludeExtRadio.setText(_translate("Dialog", "Exclude"))
        self.includeExtRadio.setText(_translate("Dialog", "Include"))
        self.searchBtn.setText(_translate("Dialog", "Search"))
        self.tabView.setTabText(self.tabView.indexOf(self.searchTab), _translate("Dialog", "Search environnement"))
        self.label.setText(_translate("Dialog", "Duplicate list :"))
        self.label_4.setText(_translate("Dialog", "Folder order to delete duplicated files (double clic on a folder on the upper list to add it):"))
        self.rankDelBtn.setText(_translate("Dialog", "Delete"))
        self.rankUpBtn.setText(_translate("Dialog", "Up"))
        self.rankDownBtn.setText(_translate("Dialog", "Down"))
        self.updFolderOrderBtn.setText(_translate("Dialog", "Update"))
        self.cleanBtn.setText(_translate("Dialog", "Clean !"))
        self.tabView.setTabText(self.tabView.indexOf(self.duplicateTab), _translate("Dialog", "Search results"))
        self.label_3.setText(_translate("Dialog", "TriTout v0.1 - By Samyx"))


"""

----------------------------- DEBUT FONCTIONS A COPIER ---------------------------

"""
def infoBox(dial, txt, title="Info"):
    QtWidgets.QMessageBox.information(dial, title, txt)


def confirmBox(dial, txt, title="Confim"):
    QtWidgets.QDialogButtonBox(
        [QtWidgets.QDialogButtonBox.Ok, QtWidgets.QDialogButtonBox.Abort])


def selectFolderClicked():
    fold = str(QtWidgets.QFileDialog.getExistingDirectory(
        Dialog, "Add a directory"))

    # Vérifie qu'il a bien choisi un dossier dans la fenêtre
    if len(fold):
        fold = os.path.abspath(fold)
        ui.folderListWidget.addItems([fold])
        ui.folders.append(fold)


def incrProgressBar(i):
    val = ui.progressBar.value()
    if val <= 100-i:
        ui.progressBar.setValue(val + i)
    else:
        ui.progressBar.setValue(100)


"""
Construit un élément de ListWidget checkable
"""
def checkableItem(text):
    it = QtWidgets.QListWidgetItem(text)
    it.setFlags(
        it.flags() | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
    it.setCheckState(QtCore.Qt.Unchecked)

    return it


def searchClicked():
    # Liste des dossiers non vide et au moins une extension incluse (ou rien d'exclu)
    if ui.folderListWidget.count() != 0 and not (ui.includeExtRadio.isChecked() and ui.extInput.text() == ""):
        ui.progressBar.setEnabled(True)

        # Désactive les tabs le temps de la recherche
        ui.tabView.setEnabled(False)

        oldFolderNum = len(ui.folders)

        fileList = mapFiles2(ui.folders, ui.recursiveBox.checkState(),
                             ui.extInput.text().replace(" ", "").split(","),
                             ui.includeExtRadio.isChecked())

        # Ajoute les dossiers trouvés récursivement à la liste (même si disabled)
        ui.folderListWidget.addItems(ui.folders[oldFolderNum:])

        ui.dupFiles = findDuplicates2(ui.folders, fileList, incrProgressBar)

        if len(ui.dupFiles):
            for e in ui.dupFiles:
                # Infos fichier
                formStr = "{} - {} kb - Last modified: {}".format(
                    e[0][0], "%.2f" % round(e[0][1]/1000, 2), time.ctime(e[0][2]))
                ui.duplicateListWidget.addItem(formStr)

                # Pour chaque chemin
                for fold in e[1]:
                    ui.duplicateListWidget.addItem(checkableItem(" " + fold))

            ui.tabView.setEnabled(True)
            ui.tabView.setCurrentIndex(1)

            infoBox(Dialog, "{} duplicate(s) found !".format(len(ui.dupFiles)))
            ui.duplicateTab.setEnabled(True)
            ui.progressBar.setValue(0)

        else:
            infoBox(Dialog, "No duplicated files found !")
            ui.tabView.setEnabled(True)

    elif ui.folderListWidget.count() == 0:
        infoBox(Dialog, "You need to select at least one folder to search duplicates")

    else:
        infoBox(
            Dialog, "You need to include at least one extension (or exclude nothing)")


def rankUpClicked():
    row = ui.folderOrderListWidget.currentRow()

    # Au moins un selectionné et pas le premier
    if row > 0:
        txt = ui.folderOrderListWidget.currentItem().text()

        ui.folderOrderListWidget.takeItem(row)
        ui.folderOrderListWidget.insertItem(row-1, txt)
        ui.folderOrderList[row], ui.folderOrderList[row -
                                                    1] = ui.folderOrderList[row-1], ui.folderOrderList[row]

        # Pratique: on conserve la selection du même item
        ui.folderOrderListWidget.setCurrentRow(row-1)


def rankDownClicked():
    row = ui.folderOrderListWidget.currentRow()

    # Au moins un selectionné et pas le dernier
    if row > -1 and row < ui.folderOrderListWidget.count() - 1:
        txt = ui.folderOrderListWidget.currentItem().text()

        ui.folderOrderListWidget.takeItem(row)
        ui.folderOrderListWidget.insertItem(row+1, txt)
        ui.folderOrderList[row], ui.folderOrderList[row +
                                                    1] = ui.folderOrderList[row+1], ui.folderOrderList[row]

        # Pratique: on conserve la selection du même item
        ui.folderOrderListWidget.setCurrentRow(row+1)


def rankDelClicked():
    row = ui.folderOrderListWidget.currentRow()
    if row > -1:
        ui.folderOrderListWidget.takeItem(row)
        ui.folderOrderList.pop(row)


def cleanClicked():
    # Récuperer les chemins qui sont cochés
    delList = []
    tmpFile = ""
    fileCpt = 0  # Compte l'index du fichier dans ui.dupFiles

    checkableFold = 0
    checkedFold = 0
    noDupList = []

    for i in range(ui.duplicateListWidget.count()):
        it = ui.duplicateListWidget.item(i)

        # Fichier
        if it.text()[0] != " ":
            tmpFile = ui.dupFiles[fileCpt][0][0]
            fileCpt += 1

            # Contrôle de la suppression des derniers chemins d'un fichier (suppression définitive)
            print(checkedFold, checkableFold)
            if checkableFold == checkedFold and checkedFold != 0:
                noDupList.append(ui.dupFiles[fileCpt][0][0])  # Nom du fichier

        # Dossier pas désactivé
        elif it.flags() & QtCore.Qt.ItemIsEnabled:
            checkableFold += 1

            # Dossier coché
            if it.checkState():
                delList.append(os.path.join(it.text()[1:], tmpFile))
                checkedFold += 1

    # Pas après confirmation
    if not ui.cleanNeedConfirm:
        # Contrôle de la suppression des derniers chemins d'un fichier (suppression définitive)
        print(checkedFold, checkableFold)
        if checkableFold == checkedFold and checkedFold != 0:
            noDupList.append(ui.dupFiles[fileCpt-1][0][0])  # Nom du fichier

        print(noDupList)
        if len(noDupList):
            ui.cleanNeedConfirm = True
            infoBox(Dialog, "These file(s) will be deleted forever :\n" +
                    "\n".join(noDupList) + "\nPress Clean button if you want to proceed.")
            return 0

    if len(delList):
        # Freeze la gui
        ui.tabView.setEnabled(False)
        deletedList, delCpt, delError = delFiles(delList, incrProgressBar)

        # Désactiver les éléments supprimés
        tmpFile = ""
        fileCpt = 0  # Compte l'index du fichier dans ui.dupFiles

        for i in range(ui.duplicateListWidget.count()):
            item = ui.duplicateListWidget.item(i)
            text = item.text()

            # Fichier
            if text[0] != " ":
                tmpFile = ui.dupFiles[fileCpt][0][0]
                fileCpt += 1

            # Dossier supprimé, on le désactive dans la liste et on le supprime de ui.dupFiles
            elif os.path.join(text[1:], tmpFile) in deletedList:
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEnabled)
                item.setText(text + " - Deleted")

        if delError:
            infoBox(
                Dialog, "One or more file(s) were not deleted because they are used.")

        ui.progressBar.setValue(100)
        infoBox(Dialog, "{} files deleted !".format(delCpt))
        ui.progressBar.setValue(0)
        ui.tabView.setEnabled(True)
        ui.cleanNeedConfirm = False

    else:
        infoBox(Dialog, "Please select files to proceed")


def addFolderClicked(item):
    txt = item.text()

    # Pour un dossier : l'ajouter à la liste des filtres par dossier
    if txt[0] == " ":
        if txt[1:] not in ui.folderOrderList:
            ui.folderOrderList.append(txt[1:])
            ui.folderOrderListWidget.addItem(txt[1:])

    # Pour un fichier : l'ouvrir avec l'application par défaut de l'os
    else:
        # Comme il faut le choisir dans un dossier, on prend le premier
        nextFold = ui.duplicateListWidget.item(
            ui.duplicateListWidget.currentRow() + 1)
        p = os.path.join(nextFold.text()[1:], txt)
        os.system("start " + p)


"""
Change les checkbox de la liste des doublons en fonction de l'ordre
choisi des dossiers (en laissant au moins un fichier)
"""
def updateFolderOrderClicked():
    for i in range(ui.duplicateListWidget.count()):
        item = ui.duplicateListWidget.item(i)
        text = item.text()

        # Fichier
        if text[0] != " ":
            tmpFile = text

        # Dossier de suppression (version simple: tout les doublons de ce dossier seront cochés)
        elif text[1:] in ui.folderOrderList:
            item.setCheckState(QtCore.Qt.Checked)

def advFiltersChecked():
    if ui.advFiltersGroupBox.isChecked():
        ui.advFiltersGroupBox.setMaximumHeight(ui.advFilterExpandedHeight)
    else:
        ui.advFiltersGroupBox.setMaximumHeight(ui.advFilterCollapsedHeight)

def sizeFilterChecked():
    ui.filesizeLayout.setEnabled(ui.sizeFilterBox.isChecked())

def extFilterChecked():
    ui.extLayout.setEnabled(ui.extFilterBox.isChecked())

def modifFilterChecked():
    ui.modifdateLayout.setEnabled(ui.modifFilterBox.isChecked())

"""

----------------------------- FIN FONCTIONS A COPIER ---------------------------

"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    # Connecteurs signaux/fonctions
    ui.selectFolderBtn.clicked.connect(selectFolderClicked)
    ui.searchBtn.clicked.connect(searchClicked)
    ui.rankUpBtn.clicked.connect(rankUpClicked)
    ui.rankDownBtn.clicked.connect(rankDownClicked)
    ui.rankDelBtn.clicked.connect(rankDelClicked)
    ui.cleanBtn.clicked.connect(cleanClicked)
    ui.duplicateListWidget.itemDoubleClicked.connect(addFolderClicked)
    ui.updFolderOrderBtn.clicked.connect(updateFolderOrderClicked)
    ui.advFiltersGroupBox.toggled.connect(advFiltersChecked)
    ui.extFilterBox.toggled.connect(extFilterChecked)
    ui.sizeFilterBox.toggled.connect(sizeFilterChecked)
    ui.modifFilterBox.toggled.connect(modifFilterChecked)

    # --- à déplacer de chaque gen_gui ---

    recSearch = False

    Dialog.show()
    sys.exit(app.exec_())
