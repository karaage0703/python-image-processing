import pytest
from extract_color import extract_color
import numpy as np

import cv2


# テスト用のダミー画像を生成するヘルパー関数
def create_dummy_image(width, height, color):
    image = np.zeros((height, width, 3), dtype=np.uint8)
    image[:] = color
    return image


# テストケース1: h_th_lowがh_th_upより低い場合
def test_extract_color_low_high():
    # 画像を生成（ここでは青色の画像）
    src = create_dummy_image(100, 100, (255, 0, 0))
    h_th_low = 50
    h_th_up = 100
    s_th = 50
    v_th = 50

    # extract_colorを実行
    result = extract_color(src, h_th_low, h_th_up, s_th, v_th)

    # 想定される結果を計算
    expected = np.zeros((100, 100), dtype=np.uint8)
    # 青色はHSVでHが約120なので、結果は黒（すべてのピクセルが0）になるはずです

    # 結果のアサーション
    assert np.array_equal(result, expected), "The extract_color function did not perform as expected with low < high."

# テストケース2: h_th_lowがh_th_upより高い場合
def test_extract_color_high_low():
    # 画像を生成（ここでは緑色の画像）
    src = create_dummy_image(100, 100, (0, 255, 0))
    h_th_low = 70
    h_th_up = 50
    s_th = 50
    v_th = 50

    # extract_colorを実行
    result = extract_color(src, h_th_low, h_th_up, s_th, v_th)

    # 想定される結果を計算
    expected = np.zeros((100, 100), dtype=np.uint8)

    # 結果のアサーション
    assert np.array_equal(result, expected), "The extract_color function did not perform as expected with high > low."


# テストケース3: s_thとv_thの閾値チェック
def test_extract_color_sv_threshold():
    # 彩度が低く、明度が高い色（白に近い色）の画像を生成
    src = create_dummy_image(100, 100, (128, 128, 128))
    h_th_low = 20
    h_th_up = 30
    s_th = 100  # 彩度の閾値を高く設定
    v_th = 100  # 明度の閾値を低く設定

    # extract_colorを実行
    result = extract_color(src, h_th_low, h_th_up, s_th, v_th)

    # 想定される結果を計算
    expected = np.zeros((100, 100), dtype=np.uint8)  # 閾値が高いので、全てのピクセルは除外されるべき

    # 結果のアサーション
    assert np.array_equal(result, expected), "The s_th and v_th thresholds did not filter out the pixels correctly."


# テストケース5: ソース画像がNoneの場合
def test_extract_color_with_none_image():
    with pytest.raises(cv2.error):
        extract_color(None, 50, 100, 50, 100)
