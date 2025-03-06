import os

from easy_image_processor import to_grayscale, resize_image

def test_to_grayscale():
    to_grayscale("test_input.jpg", "test_output.jpg")
    assert os.path.exists("test_output.jpg")

def test_resize_image():
    resize_image("test_input.jpg", "test_output.jpg", 100, 100)
    assert os.path.exists("test_resized.jpg")