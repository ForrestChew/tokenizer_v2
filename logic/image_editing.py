import cv2 as cv


image_styles = ["Cartoonify", "Borders", "No style"]


def adaptive_threshold_style(img_file_path: str) -> None:
    img = cv.imread(img_file_path, cv.IMREAD_COLOR)
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    adaptive_thresh = cv.adaptiveThreshold(
        gray_img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 7
    )
    styled_img_file_name = "stylized.png"
    cv.imwrite(styled_img_file_name, adaptive_thresh)


def cartoonify_style(image_file_path: str) -> None:
    img = cv.imread(image_file_path)
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    adaptive_threshold = cv.adaptiveThreshold(
        gray_img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 7
    )
    dst = cv.edgePreservingFilter(img, flags=2, sigma_s=64, sigma_r=0.5)
    complete_style = cv.bitwise_and(dst, dst, mask=adaptive_threshold)
    styled_img_file_name = "stylized.png"
    cv.imwrite(styled_img_file_name, complete_style)
