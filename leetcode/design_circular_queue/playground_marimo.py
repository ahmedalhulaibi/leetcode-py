import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_circular_queue, run_circular_queue
    from solution import MyCircularQueue

    return MyCircularQueue, assert_circular_queue, run_circular_queue


@app.cell
def _():
    # Example test case
    operations = [
        "MyCircularQueue",
        "en_queue",
        "en_queue",
        "en_queue",
        "en_queue",
        "rear",
        "is_full",
        "de_queue",
        "en_queue",
        "rear",
    ]
    inputs = [[3], [1], [2], [3], [4], [], [], [], [4], []]
    expected = [None, True, True, True, False, 3, True, True, True, 4]
    return expected, inputs, operations


@app.cell
def _(MyCircularQueue, inputs, operations, run_circular_queue):
    result, queue = run_circular_queue(MyCircularQueue, operations, inputs)
    print(result)
    queue
    return (result,)


@app.cell
def _(assert_circular_queue, expected, result):
    assert_circular_queue(result, expected)
    return


if __name__ == "__main__":
    app.run()
