from typing import Callable, Tuple
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from .ui_component_styles import label_area_unactive, image_pop_up
from logic.slots import ButtonSlots


class UiComponents(ButtonSlots):
    def __init__(self):
        self.right_gb, self.right_label = self.create_group_box_area(
            "Image Minting", "Stage an image \n in order to mint it"
        )
        self.left_gb, self.left_label = self.create_group_box_area(
            "Image Staging", "Click the browse \n button to load image"
        )
        self.enlarge_browsed_img_btn = self.create_secondary_button(
            "Enlarge Browsed Image",
            lambda: self.create_image_pop_up(self.browsed_image),
        )
        self.enlarge_staged_img_btn = self.create_secondary_button(
            "Enlarge Staged Image", lambda: self.create_image_pop_up(self.styled_img)
        )

    def create_primary_button(
        self, title: str, button_clicked_action: Callable[[qtw.QLabel], None]
    ) -> qtw.QPushButton:
        button = qtw.QPushButton(title)
        button.setFixedWidth(100)
        button.setFixedHeight(50)
        button.clicked.connect(button_clicked_action)

        return button

    def create_secondary_button(
        self, title: str, button_clicked_action: Callable[[str], None]
    ) -> qtw.QPushButton:
        button = qtw.QPushButton(title)
        button.setEnabled(False)
        button.clicked.connect(button_clicked_action)

        return button

    def create_img_area_label(self, title: str) -> qtw.QLabel:
        label = qtw.QLabel()
        label.setGeometry(0, 0, 1600, 768)
        label.setAlignment(qtc.Qt.AlignCenter)
        label.setText(title)
        label.setFont(qtg.QFont("Monospace", 16))
        label.setStyleSheet(label_area_unactive)

        return label

    def create_image_pop_up(self, image: qtg.QPixmap) -> None:
        self.label = qtw.QLabel()
        self.label.setGeometry(10, 10, 1440, 810)
        self.label.setStyleSheet(image_pop_up)
        self.scaled_pixmap = image.scaled(1440, 810, qtc.Qt.KeepAspectRatio)
        self.label.setPixmap(self.scaled_pixmap)
        self.label.show()

    def create_group_box_area(
        self, gb_title: str, label_title: str
    ) -> Tuple[qtw.QGroupBox, qtw.QLabel]:
        group_box = qtw.QGroupBox(gb_title)
        label = self.create_img_area_label(label_title)

        return group_box, label

    def create_left_window_area(self) -> qtw.QGroupBox:
        style_select_menu = qtw.QComboBox()
        style_select_menu.addItems(
            ["Select Style", "Borders", "Cartoonify", "No style"]
        )
        left_gb_options_layout = qtw.QGridLayout()
        left_gb_options_layout.addWidget(
            self.create_primary_button(
                "Browse",
                lambda: self.browse_image(
                    self.left_label, self.enlarge_browsed_img_btn
                ),
            ),
            0,
            0,
            2,
            1,
        )
        left_gb_options = qtw.QGroupBox()
        left_gb_options.setLayout(left_gb_options_layout)
        left_gb_main_layout = qtw.QVBoxLayout()
        left_gb_main_layout.addWidget(self.left_label, 5)
        left_gb_main_layout.addWidget(self.enlarge_browsed_img_btn)
        left_gb_options_layout.addWidget(style_select_menu, 0, 2, 2, 1)
        left_gb_options_layout.addWidget(
            self.create_primary_button(
                "Stage",
                lambda: self.stage_image(
                    self.right_label,
                    str(style_select_menu.currentText()),
                    self.enlarge_staged_img_btn,
                ),
            ),
            0,
            3,
            2,
            1,
        )
        left_gb_main_layout.addWidget(left_gb_options, 1)
        self.left_gb.setLayout(left_gb_main_layout)

        return self.left_gb

    def create_right_window_area(self) -> qtw.QGroupBox:
        nft_name_input = qtw.QLineEdit()
        nft_name_input.setPlaceholderText("NFT name")
        nft_description_input = qtw.QLineEdit()
        nft_description_input.setPlaceholderText("NFT description")
        right_gb_options_layout = qtw.QGridLayout()
        right_gb_options_layout.addWidget(
            self.create_primary_button(
                "Delete", lambda: self.clear_image(self.right_label)
            ),
            0,
            0,
            2,
            1,
        )
        right_gb_options_layout.addWidget(nft_name_input, 0, 1)
        right_gb_options_layout.addWidget(nft_description_input, 1, 1)
        right_gb_options_layout.addWidget(
            self.create_primary_button(
                "Mint",
                lambda: self.mint_image(
                    nft_name_input.text(),
                    nft_description_input.text(),
                ),
            ),
            0,
            2,
            2,
            1,
        )
        right_gb_options = qtw.QGroupBox()
        right_gb_options.setLayout(right_gb_options_layout)
        right_gb_main_layout = qtw.QVBoxLayout()
        right_gb_main_layout.addWidget(self.right_label, 5)
        right_gb_main_layout.addWidget(self.enlarge_staged_img_btn)
        right_gb_main_layout.addWidget(right_gb_options, 1)
        self.right_gb.setLayout(right_gb_main_layout)

        return self.right_gb
