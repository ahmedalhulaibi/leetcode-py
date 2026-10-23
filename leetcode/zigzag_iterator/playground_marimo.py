import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_zigzag_iterator, run_zigzag_iterator
    from solution import ZigzagIterator

    return ZigzagIterator, assert_zigzag_iterator, run_zigzag_iterator


@app.cell
def _():
    # Example test case
    operations = ["ZigzagIterator", "next", "next", "next", "next", "next", "next", "has_next"]
    inputs = [[[1, 2], [3, 4, 5, 6]], [], [], [], [], [], [], []]
    expected = [None, 1, 3, 2, 4, 5, 6, False]
    return expected, inputs, operations


@app.cell
def _(ZigzagIterator, inputs, operations, run_zigzag_iterator):
    result, iterator = run_zigzag_iterator(ZigzagIterator, operations, inputs)
    print(result)
    iterator
    return (result,)


@app.cell
def _(assert_zigzag_iterator, expected, result):
    assert_zigzag_iterator(result, expected)
    return


if __name__ == "__main__":
    app.run()
