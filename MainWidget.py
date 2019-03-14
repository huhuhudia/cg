'''
Created on 2018年8月8日

@author: Freedom
'''
from PyQt5.Qt import QWidget, QColor, QPixmap, QIcon, QSize, QCheckBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QSplitter,\
    QComboBox, QLabel, QSpinBox, QFileDialog
from PaintBoard import PaintBoard

class MainWidget(QWidget):


    def __init__(self, Parent=None):
        '''
        Constructor
        '''
        super().__init__(Parent)
        
        self.__InitData() #先初始化数据，再初始化界面
        self.__InitView()
    
    def __InitData(self):
        '''
                  初始化成员变量
        '''
        self.__paintBoard = PaintBoard(self)
        self.__colorList = QColor.colorNames() #获取颜色列表(字符串类型)
        
    def __InitView(self):
        '''
                  初始化界面
        '''
        self.setFixedSize(2560,1600)
        self.setWindowTitle("图形学画板")
        

        main_layout = QHBoxLayout(self) #新建一个水平布局作为本窗体的主布局
        main_layout.setSpacing(10) #设置主布局内边距以及控件间距为10px

        sub_layout_LEVEL1 = QVBoxLayout() #新建垂直子布局用于放置按键
        sub_layout_LEVEL1.setContentsMargins(10, 10, 10, 10) #设置此子布局和内部控件的间距为10px
        main_layout.addLayout(sub_layout_LEVEL1) #将子布局1加入主布局

        sub_layout_LEVEL2 = QVBoxLayout()  # 新建垂直子布局用于放置按键
        sub_layout_LEVEL2.setContentsMargins(10, 10, 10, 10)  # 设置此子布局和内部控件的间距为10px
        main_layout.addLayout(sub_layout_LEVEL2)  # 将子布局2加入主布局

        sub_layout_LEVEL3 = QVBoxLayout()  # 新建垂直子布局用于放置按键
        sub_layout_LEVEL3.setContentsMargins(10, 10, 10, 10)  # 设置此子布局和内部控件的间距为10px
        main_layout.addLayout(sub_layout_LEVEL3)  # 将子布局2加入主布局

        sub_layout_LEVEL2_1 = QHBoxLayout()  # 新建水平子布局用于放置按键
        sub_layout_LEVEL2_1.setContentsMargins(10, 10, 10, 10)  # 设置此子布局和内部控件的间距为10px
        sub_layout_LEVEL2.addLayout(sub_layout_LEVEL2_1)

        sub_layout_LEVEL2_2 = QHBoxLayout()  # 新建水平子布局用于放置按键
        sub_layout_LEVEL2_2.setContentsMargins(10, 10, 10, 10)  # 设置此子布局和内部控件的间距为10px
        sub_layout_LEVEL2.addLayout(sub_layout_LEVEL2_2)

        sub_layout_LEVEL2_3 = QHBoxLayout()  # 新建水平子布局用于放置按键
        sub_layout_LEVEL2_3.setContentsMargins(10, 10, 10, 10)  # 设置此子布局和内部控件的间距为10px
        sub_layout_LEVEL2.addLayout(sub_layout_LEVEL2_3)

        sub_layout_LEVEL2_4 = QHBoxLayout()  # 新建水平子布局用于放置按键
        sub_layout_LEVEL2_4.setContentsMargins(10, 10, 10, 10)  # 设置此子布局和内部控件的间距为10px
        sub_layout_LEVEL2.addLayout(sub_layout_LEVEL2_4)

        #放置左侧图标
        self.__btn_Quit = QPushButton("    退出")
        self.__btn_Quit.setIcon(QIcon("1.png"))  # 设置图标
        self.__btn_Quit.setFixedHeight(60)
        self.__btn_Quit.setFixedWidth(200)
        self.__btn_Quit.setParent(self) #设置父对象为本界面
        self.__btn_Quit.clicked.connect(self.Quit)
        sub_layout_LEVEL1.addWidget(self.__btn_Quit)
        
        self.__btn_Save = QPushButton("保存作品")
        self.__btn_Save.setIcon(QIcon("1.png"))  # 设置图标
        self.__btn_Save.setFixedHeight(60)
        self.__btn_Save.setFixedWidth(200)
        self.__btn_Save.setParent(self)
        self.__btn_Save.clicked.connect(self.on_btn_Save_Clicked)
        sub_layout_LEVEL1.addWidget(self.__btn_Save)

        self.__btn_Load = QPushButton("读取作品")
        self.__btn_Load.setIcon(QIcon("1.png"))  # 设置图标
        self.__btn_Load.setFixedHeight(60)
        self.__btn_Load.setFixedWidth(200)
        self.__btn_Load.setParent(self)
        self.__btn_Load.clicked.connect(self.on_btn_Load_Clicked)
        sub_layout_LEVEL1.addWidget(self.__btn_Load)

        splitter = QSplitter(self) #占位符
        sub_layout_LEVEL1.addWidget(splitter)

        self.__cbtn_drawline=QPushButton("    直线")
        self.__cbtn_drawline.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_drawline.setFixedHeight(60)
        self.__cbtn_drawline.setFixedWidth(200)
        self.__cbtn_drawline.setParent(self)
        self.__cbtn_drawline.clicked.connect(self.on_cbtn_drawline_clicked)
        sub_layout_LEVEL1.addWidget(self.__cbtn_drawline)

        self.__cbtn_zhexian = QPushButton("    折线")
        self.__cbtn_zhexian.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_zhexian.setFixedHeight(60)
        self.__cbtn_zhexian.setFixedWidth(200)
        self.__cbtn_zhexian.setParent(self)
        self.__cbtn_zhexian.clicked.connect(self.on_cbtn_zhexian_clicked)
        sub_layout_LEVEL1.addWidget(self.__cbtn_zhexian)

        self.__cbtn_zhijiaoxian = QPushButton("  直角线")
        self.__cbtn_zhijiaoxian.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_zhijiaoxian.setFixedHeight(60)
        self.__cbtn_zhijiaoxian.setFixedWidth(200)
        self.__cbtn_zhijiaoxian.setParent(self)
        self.__cbtn_zhijiaoxian.clicked.connect(self.on_cbtn_zhijiaoxian_clicked)
        sub_layout_LEVEL1.addWidget(self.__cbtn_zhijiaoxian)

        self.__cbtn_duobianxing = QPushButton("  多边形")
        self.__cbtn_duobianxing.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_duobianxing.setFixedHeight(60)
        self.__cbtn_duobianxing.setFixedWidth(200)
        self.__cbtn_duobianxing.setParent(self)
        self.__cbtn_duobianxing.clicked.connect(self.on_cbtn_duobianxing_clicked)
        sub_layout_LEVEL1.addWidget(self.__cbtn_duobianxing)

        self.__cbtn_circle = QPushButton("  圆    ")
        self.__cbtn_circle.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_circle.setFixedHeight(60)
        self.__cbtn_circle.setFixedWidth(200)
        self.__cbtn_circle.setParent(self)
        self.__cbtn_circle.clicked.connect(self.on_cbtn_circle_clicked)
        sub_layout_LEVEL1.addWidget(self.__cbtn_circle)

        self.__cbtn_oval = QPushButton("    椭圆")
        self.__cbtn_oval.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_oval.setFixedHeight(60)
        self.__cbtn_oval.setFixedWidth(200)
        self.__cbtn_oval.setParent(self)
        self.__cbtn_oval.clicked.connect(self.on_cbtn_oval_clicked)
        sub_layout_LEVEL1.addWidget(self.__cbtn_oval)

        self.__cbtn_yuanhu = QPushButton("    圆弧")
        self.__cbtn_yuanhu.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_yuanhu.setFixedHeight(60)
        self.__cbtn_yuanhu.setFixedWidth(200)
        self.__cbtn_yuanhu.setParent(self)
        self.__cbtn_yuanhu.clicked.connect(self.on_cbtn_yuanhu_clicked)
        sub_layout_LEVEL1.addWidget(self.__cbtn_yuanhu)

        self.__cbtn_tuoyuanhu = QPushButton("  椭圆弧")
        self.__cbtn_tuoyuanhu.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_tuoyuanhu.setFixedHeight(60)
        self.__cbtn_tuoyuanhu.setFixedWidth(200)
        self.__cbtn_tuoyuanhu.setParent(self)
        self.__cbtn_tuoyuanhu.clicked.connect(self.on_cbtn_tuoyuanhu_clicked)
        sub_layout_LEVEL1.addWidget(self.__cbtn_tuoyuanhu)

        self.__cbtn_renyiquxian = QPushButton("任意曲线")
        self.__cbtn_renyiquxian.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_renyiquxian.setFixedHeight(60)
        self.__cbtn_renyiquxian.setFixedWidth(200)
        self.__cbtn_renyiquxian.setParent(self)
        self.__cbtn_renyiquxian.clicked.connect(self.on_cbtn_renyiquxian_clicked)
        sub_layout_LEVEL1.addWidget(self.__cbtn_renyiquxian)

        self.__cbtn_smooth_rectangle = QPushButton("圆角矩形")
        self.__cbtn_smooth_rectangle.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_smooth_rectangle.setFixedHeight(60)
        self.__cbtn_smooth_rectangle.setFixedWidth(200)
        self.__cbtn_smooth_rectangle.setParent(self)
        self.__cbtn_smooth_rectangle.clicked.connect(self.on_cbtn_smooth_rectangle_clicked)
        sub_layout_LEVEL1.addWidget(self.__cbtn_smooth_rectangle)

        self.__cbtn_rectangle = QPushButton("    矩形")
        self.__cbtn_rectangle.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_rectangle.setFixedHeight(60)
        self.__cbtn_rectangle.setFixedWidth(200)
        self.__cbtn_rectangle.setParent(self)
        self.__cbtn_rectangle.clicked.connect(self.on_cbtn_rectangle_clicked)
        sub_layout_LEVEL1.addWidget(self.__cbtn_rectangle)

        self.__cbtn_character = QPushButton("    字符")
        self.__cbtn_character.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_character.setFixedHeight(60)
        self.__cbtn_character.setFixedWidth(200)
        self.__cbtn_character.setParent(self)
        self.__cbtn_character.clicked.connect(self.on_cbtn_character_clicked)
        sub_layout_LEVEL1.addWidget(self.__cbtn_character)

        splitter = QSplitter(self) #占位符
        sub_layout_LEVEL1.addWidget(splitter)

        self.__cbtn_Eraser = QCheckBox("橡皮擦")
        self.__cbtn_Eraser.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_Eraser.setFixedHeight(60)
        self.__cbtn_Eraser.setFixedWidth(200)
        self.__cbtn_Eraser.setParent(self)
        self.__cbtn_Eraser.clicked.connect(self.on_cbtn_Eraser_clicked)
        sub_layout_LEVEL1.addWidget(self.__cbtn_Eraser)

        self.__btn_Clear = QPushButton("清空画板")
        self.__btn_Clear.setParent(self)  # 设置父对象为本界面
        self.__btn_Clear.setIcon(QIcon("1.png"))  # 设置图标
        self.__btn_Clear.setFixedHeight(60)
        self.__btn_Clear.setFixedWidth(200)
        self.__btn_Clear.clicked.connect(self.__paintBoard.Clear)  # 将按键按下信号与画板清空函数相关联
        sub_layout_LEVEL1.addWidget(self.__btn_Clear)

        splitter = QSplitter(self) #占位符
        sub_layout_LEVEL1.addWidget(splitter)

        self.__label_penThickness = QLabel(self)
        self.__label_penThickness.setText("画笔粗细")
        self.__label_penThickness.setFixedHeight(60)
        self.__label_penThickness.setFixedWidth(200)
        sub_layout_LEVEL1.addWidget(self.__label_penThickness)
        
        self.__spinBox_penThickness = QSpinBox(self)
        self.__spinBox_penThickness.setFixedHeight(60)
        self.__spinBox_penThickness.setFixedWidth(200)
        self.__spinBox_penThickness.setMaximum(20)
        self.__spinBox_penThickness.setMinimum(2)
        self.__spinBox_penThickness.setValue(10) #默认粗细为10
        self.__spinBox_penThickness.setSingleStep(2) #最小变化值为1
        self.__spinBox_penThickness.valueChanged.connect(self.on_PenThicknessChange)#关联spinBox值变化信号和函数on_PenThicknessChange
        sub_layout_LEVEL1.addWidget(self.__spinBox_penThickness)

        self.__label_penThickness = QLabel(self)
        self.__label_penThickness.setText("选择颜色")
        self.__label_penThickness.setFixedHeight(60)
        self.__label_penThickness.setFixedWidth(200)
        sub_layout_LEVEL1.addWidget(self.__label_penThickness)
        
        self.__comboBox_penColor = QComboBox(self)
        self.__comboBox_penColor.setFixedHeight(60)
        self.__comboBox_penColor.setFixedWidth(200)
        self.__fillColorList(self.__comboBox_penColor) #用各种颜色填充下拉列表
        self.__comboBox_penColor.currentIndexChanged.connect(self.on_PenColorChange) #关联下拉列表的当前索引变更信号与函数on_PenColorChange
        sub_layout_LEVEL1.addWidget(self.__comboBox_penColor)

        self.__btn_fillcolor = QPushButton("填充颜色")
        self.__btn_fillcolor.setIcon(QIcon("1.png"))  # 设置图标
        self.__btn_fillcolor.setFixedHeight(60)
        self.__btn_fillcolor.setFixedWidth(200)
        self.__btn_fillcolor.setParent(self)
        self.__btn_fillcolor.clicked.connect(self.on_btn_fillcolor_Clicked)
        sub_layout_LEVEL1.addWidget(self.__btn_fillcolor)

        #放置中间图标
        sub_layout_LEVEL2_2.addWidget(self.__paintBoard)#放置画板

        self.__cbtn_recall = QPushButton("    撤回")
        self.__cbtn_recall.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_recall.setFixedHeight(60)
        self.__cbtn_recall.setFixedWidth(200)
        self.__cbtn_recall.setParent(self)
        self.__cbtn_recall.clicked.connect(self.on_cbtn_recall_clicked)
        sub_layout_LEVEL2_3.addWidget(self.__cbtn_recall)

        self.__cbtn_repetition = QPushButton("    重复")
        self.__cbtn_repetition.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_repetition.setFixedHeight(60)
        self.__cbtn_repetition.setFixedWidth(200)
        self.__cbtn_repetition.setParent(self)
        self.__cbtn_repetition.clicked.connect(self.on_cbtn_repetition_clicked)
        sub_layout_LEVEL2_3.addWidget(self.__cbtn_repetition)

        self.__cbtn_aim_left = QPushButton("  左对齐")
        self.__cbtn_aim_left.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_aim_left.setFixedHeight(60)
        self.__cbtn_aim_left.setFixedWidth(200)
        self.__cbtn_aim_left.setParent(self)
        self.__cbtn_aim_left.clicked.connect(self.on_cbtn_aim_left_clicked)
        sub_layout_LEVEL2_1.addWidget(self.__cbtn_aim_left)

        self.__cbtn_aim_middle = QPushButton("中间对齐")
        self.__cbtn_aim_middle.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_aim_middle.setFixedHeight(60)
        self.__cbtn_aim_middle.setFixedWidth(200)
        self.__cbtn_aim_middle.setParent(self)
        self.__cbtn_aim_middle.clicked.connect(self.on_cbtn_aim_middle_clicked)
        sub_layout_LEVEL2_1.addWidget(self.__cbtn_aim_middle)

        self.__cbtn_aim_right = QPushButton("  右对齐")
        self.__cbtn_aim_right.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_aim_right.setFixedHeight(60)
        self.__cbtn_aim_right.setFixedWidth(200)
        self.__cbtn_aim_right.setParent(self)
        self.__cbtn_aim_right.clicked.connect(self.on_cbtn_aim_right_clicked)
        sub_layout_LEVEL2_1.addWidget(self.__cbtn_aim_right)

        self.__cbtn_cut_inside = QPushButton("  内裁剪")
        self.__cbtn_cut_inside.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_cut_inside.setFixedHeight(60)
        self.__cbtn_cut_inside.setFixedWidth(200)
        self.__cbtn_cut_inside.setParent(self)
        self.__cbtn_cut_inside.clicked.connect(self.on_cbtn_cut_inside_clicked)
        sub_layout_LEVEL2_4.addWidget(self.__cbtn_cut_inside)

        self.__cbtn_cut_outside = QPushButton("  外裁剪")
        self.__cbtn_cut_outside.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_cut_outside.setFixedHeight(60)
        self.__cbtn_cut_outside.setFixedWidth(200)
        self.__cbtn_cut_outside.setParent(self)
        self.__cbtn_cut_outside.clicked.connect(self.on_cbtn_cut_outside_clicked)
        sub_layout_LEVEL2_4.addWidget(self.__cbtn_cut_outside)

        #放置右侧图标

        self.__cbtn_select = QPushButton("    选择")
        self.__cbtn_select.setIcon(QIcon("1.png"))  # 设置图标
        self.__cbtn_select.setFixedHeight(60)
        self.__cbtn_select.setFixedWidth(200)
        self.__cbtn_select.setParent(self)
        self.__cbtn_select.clicked.connect(self.on_cbtn_select_clicked)
        sub_layout_LEVEL3.addWidget(self.__cbtn_select)

    def __fillColorList(self, comboBox):

        index_black = 0
        index = 0
        for color in self.__colorList: 
            if color == "black":
                index_black = index
            index += 1
            pix = QPixmap(70,20)
            pix.fill(QColor(color))
            comboBox.addItem(QIcon(pix),None)
            comboBox.setIconSize(QSize(70,20))
            comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        comboBox.setCurrentIndex(index_black)
        
    def on_PenColorChange(self):
        color_index = self.__comboBox_penColor.currentIndex()
        color_str = self.__colorList[color_index]
        self.__paintBoard.ChangePenColor(color_str)

    def on_PenThicknessChange(self):
        penThickness = self.__spinBox_penThickness.value()
        self.__paintBoard.ChangePenThickness(penThickness)
    
    def on_btn_Save_Clicked(self):
        savePath = QFileDialog.getSaveFileName(self, 'Save Your Paint', '.\\', '*.png')
        print(savePath)
        if savePath[0] == "":
            print("Save cancel")
            return
        image = self.__paintBoard.GetContentAsQImage()
        image.save(savePath[0])
        
    def on_cbtn_Eraser_clicked(self):
        if self.__cbtn_Eraser.isChecked():
            self.__paintBoard.EraserMode = True #进入橡皮擦模式
        else:
            self.__paintBoard.EraserMode = False #退出橡皮擦模式
        
    def on_cbtn_drawline_clicked(self):
        print("划线函数")

    def on_btn_Load_Clicked(self):
        print("读取作品")

    def on_cbtn_zhexian_clicked(self):
        print("折线")

    def on_cbtn_zhijiaoxian_clicked(self):
        print("直角线")

    def on_cbtn_duobianxing_clicked(self):
        print("多边形")

    def on_cbtn_circle_clicked(self):
        print("圆")

    def on_cbtn_oval_clicked(self):
        print("椭圆")

    def on_cbtn_yuanhu_clicked(self):
        print("圆弧")

    def on_cbtn_tuoyuanhu_clicked(self):
        print("椭圆弧")

    def on_cbtn_renyiquxian_clicked(self):
        print("任意曲线")

    def on_cbtn_smooth_rectangle_clicked(self):
        print("圆角矩形")

    def on_cbtn_rectangle_clicked(self):
        print("矩形")

    def on_cbtn_character_clicked(self):
        print("字符")

    def on_cbtn_recall_clicked(self):
        print("撤回")

    def on_cbtn_repetition_clicked(self):
        print("重复")

    def on_cbtn_aim_left_clicked(self):
        print("左对齐")

    def on_cbtn_aim_middle_clicked(self):
        print("中间对齐")

    def on_cbtn_aim_right_clicked(self):
        print("右对齐")

    def on_cbtn_cut_inside_clicked(self):
        print("内裁剪")

    def on_cbtn_cut_outside_clicked(self):
        print("外裁剪")

    def on_cbtn_select_clicked(self):
        print("选择")

    def on_btn_fillcolor_Clicked(self):
        print("填充颜色")

    # def on_cbtn_drawline_clicked(self):
    #     print("划线函数")
    #
    # def on_cbtn_drawline_clicked(self):
    #     print("划线函数")
    #
    # def on_cbtn_drawline_clicked(self):
    #     print("划线函数")
    #
    # def on_cbtn_drawline_clicked(self):
    #     print("划线函数")
    #
    # def on_cbtn_drawline_clicked(self):
    #     print("划线函数")
    #
    # def on_cbtn_drawline_clicked(self):
    #     print("划线函数")

    def on_cbtn_drawline_clicked(self):
        print("划线函数")
    def Quit(self):
        self.close()
        
    
        
        
    
