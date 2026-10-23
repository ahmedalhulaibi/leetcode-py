import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_circular_deque, run_circular_deque
    from solution import MyCircularDeque

    return MyCircularDeque, assert_circular_deque, run_circular_deque


@app.cell
def _():
    # Example test case
    operations = [
        "MyCircularDeque",
        "insert_last",
        "insert_last",
        "insert_front",
        "insert_front",
        "get_rear",
        "is_full",
        "delete_last",
        "insert_front",
        "get_front",
    ]
    inputs = [[3], [1], [2], [3], [4], [], [], [], [4], []]
    expected = [None, True, True, True, False, 2, True, True, True, 4]
    return expected, inputs, operations


@app.cell
def _(MyCircularDeque, inputs, operations, run_circular_deque):
    result, deq = run_circular_deque(MyCircularDeque, operations, inputs)
    print(result)
    deq
    return (result,)


@app.cell
def _(assert_circular_deque, expected, result):
    assert_circular_deque(result, expected)
    return


if __name__ == "__main__":
    app.run()
