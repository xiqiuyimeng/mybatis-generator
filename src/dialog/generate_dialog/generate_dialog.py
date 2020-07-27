# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm_select_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
"""
点击生成按钮，弹窗页面。
第一个页面为选择表字段展示页面。
第二个页面为生成器输出配置页面
"""

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from src.dialog.generate_dialog.confirm_selected_tree_ui import TreeWidgetUI
from src.dialog.generate_dialog.path_generator_ui import PathGeneratorUI
from src.dialog.generate_dialog.project_generator_ui import ProjectGeneratorUI
from src.dialog.generate_result_dialog import GenerateResultDialog
from src.sys.settings.font import set_font


class DisplaySelectedDialog(QDialog):

    def __init__(self, gui, selected_data):
        super().__init__()
        # 维护主界面窗口对象
        self.gui = gui
        # 选中的数据，以此来渲染树
        self.selected_data = selected_data
        self._translate = _translate = QtCore.QCoreApplication.translate
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("Dialog")
        # 固定大小，不允许缩放
        self.setFixedSize(1000, 800)

        self.verticalLayout_frame = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_frame.setObjectName("verticalLayout_frame")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # 设置字体
        self.setFont(set_font())
        # 建立布局
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        # 展示已选中数据的树结构
        self.tree_widget_ui = TreeWidgetUI(self)
        self.tree_widget = self.tree_widget_ui.widget
        self.verticalLayout.addWidget(self.tree_widget)
        self.verticalLayout_frame.addWidget(self.frame)

        # 不透明度
        self.setWindowOpacity(0.95)
        # 隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置窗口背景透明
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("#frame{border-style:solid;border-radius:25px;background-color:LightYellow;}")
        QtCore.QMetaObject.connectSlotsByName(self)

    def select_project_generator(self):
        """选择项目生成器"""
        # 隐藏树控件
        self.tree_widget.hide()
        # 打开下一页
        if hasattr(self, 'project_generator_widget'):
            self.project_generator_widget.show()
        else:
            self.project_generator_widget = ProjectGeneratorUI(self).widget
            self.verticalLayout.addWidget(self.project_generator_widget)

    def select_path_generator(self):
        """选择路径生成器"""
        # 隐藏树控件
        self.tree_widget.hide()
        # 打开下一页
        if hasattr(self, 'path_generator_widget'):
            self.path_generator_widget.show()
        else:
            self.path_generator_widget = PathGeneratorUI(self).widget
            self.verticalLayout.addWidget(self.path_generator_widget)

    def generate(self, output_dict):
        dialog = GenerateResultDialog(self.gui, output_dict, self.selected_data)
        dialog.close_parent_signal.connect(self.close)
        dialog.exec()


