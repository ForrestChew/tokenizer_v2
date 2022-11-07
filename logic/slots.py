from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from . import image_editing
from . import image_minting
from ui.ui_utility_components import notification_popup
from ui.ui_component_styles import label_area_active
from ui.ui_component_styles import label_area_unactive


class ButtonSlots:
    def __init__(self):
        self.browsed_img_file_path = None
        self.browsed_image = None
        self.styled_img = None

    def browse_image(
        self, left_label: qtw.QLabel, enlarge_browsed_img_btn: qtw.QPushButton
    ) -> qtg.QPixmap:
        self.browsed_img_file_path = qtw.QFileDialog.getOpenFileName(
            None, "Select Image", None, "Image files, (*jpg *.png)"
        )[0]
        if not self.browsed_img_file_path:
            return
        self.browsed_image = qtg.QPixmap(self.browsed_img_file_path)
        left_label.setStyleSheet(label_area_active)
        scaled_pixmap = self.browsed_image.scaled(
            470,
            398,
            qtc.Qt.KeepAspectRatio,
        )
        left_label.setPixmap(scaled_pixmap)
        enlarge_browsed_img_btn.setEnabled(True)

    def stage_image(
        self,
        right_label: qtw.QLabel,
        style_select_text: str,
        enlarge_staged_img_btn: qtw.QPushButton,
    ) -> None:
        if style_select_text not in image_editing.image_styles:
            notification_popup("Please select a style", "Staging Error")
            return

        if style_select_text == "Cartoonify":
            image_editing.cartoonify_style(self.browsed_img_file_path)
            self.set_styled_image(right_label, "stylized.png", enlarge_staged_img_btn)

        elif style_select_text == "Borders":
            image_editing.adaptive_threshold_style(self.browsed_img_file_path)
            self.set_styled_image(right_label, "stylized.png", enlarge_staged_img_btn)

        else:
            self.set_styled_image(
                right_label, self.browsed_img_file_path, enlarge_staged_img_btn
            )

    def set_styled_image(
        self,
        right_label: qtw.QLabel,
        img_path: str,
        enlarge_staged_img_btn: qtw.QPushButton,
    ) -> None:
        right_label.setStyleSheet(label_area_active)
        self.styled_img = qtg.QPixmap(img_path)
        scaled_pixmap = self.styled_img.scaled(
            470,
            398,
            qtc.Qt.KeepAspectRatio,
        )
        right_label.setPixmap(scaled_pixmap)
        enlarge_staged_img_btn.setEnabled(True)

    def clear_image(self, right_label: qtw.QLabel) -> None:
        right_label.clear()
        right_label.setStyleSheet(label_area_unactive)
        right_label.setText("Stage an image \n in order to mint it")

    def mint_image(self, name_input_text: str, description_input_text: str) -> None:
        stylized_img_file_path = "./stylized.png"
        try:
            image_uri = image_minting.upload_img_to_ipfs(stylized_img_file_path)
            image_minting.upload_img_to_pinata(stylized_img_file_path)
            pinned_metadata_url = image_minting.upload_nft_metadata_to_pinata(
                name_input_text, description_input_text, image_uri
            )
            image_minting.mint_collectable(pinned_metadata_url)
            notification_popup("Mint Successful", "Mint Status")
        except Exception as e:
            print(e)
            notification_popup("Failure to mint. Please retry", "Mint Status")
