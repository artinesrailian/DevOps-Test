import utils.square as square
from unittest.mock import patch

def test_square(capsys):
    # Simulate user input of "2"
    user_inputs = ["2\n"]
    expected_output = "The square of 2 = 4\n"

    # Patch the 'input' function to return the user inputs
    with patch('builtins.input', side_effect=user_inputs):
        square.square()  # Call the function being tested

    # Capture the printed output
    captured_output, _ = capsys.readouterr()

    # Compare the captured output with the expected output
    assert captured_output == expected_output

def test_square_invalid_input(capsys):
    # Simulate user input of "abc" (invalid) and "4" (valid)
    user_inputs = ["abc\n", "4\n"]
    expected_output = "Error: Your input is not a number!\n" \
                        "The square of 4 = 16\n"

    # Patch the 'input' function to return the user inputs
    with patch('builtins.input', side_effect=user_inputs):
        square.square()  # Call the function being tested

    # Capture the printed output
    captured_output, _ = capsys.readouterr()

    # Compare the captured output with the expected output
    assert captured_output == expected_output
