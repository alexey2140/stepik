#assert abs(-42) == 42 # True assert
#assert abs(-42) == -42, "Should be absolute value of a number" # Assert with False

def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке

    num1 = expected_result

    num2 = actual_result

    assert num1 == num2, \
        f"expected {num1}, got {num2}"
