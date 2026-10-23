import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_my_queue, run_my_queue
    from solution import MyQueue

    return MyQueue, assert_my_queue, run_my_queue


@app.cell
def _():
    # Example test case
    operations = ["MyQueue", "push", "push", "peek", "pop", "empty"]
    inputs = [[], [1], [2], [], [], []]
    expected = [None, None, None, 1, 1, False]
    return expected, inputs, operations


@app.cell
def _(MyQueue, inputs, operations, run_my_queue):
    result, queue = run_my_queue(MyQueue, operations, inputs)
    print(result)
    queue
    return (result,)


@app.cell
def _(assert_my_queue, expected, result):
    assert_my_queue(result, expected)
    return


if __name__ == "__main__":
    app.run()
