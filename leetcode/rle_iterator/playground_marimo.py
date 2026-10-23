import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rle_iterator, run_rle_iterator
    from solution import RLEIterator

    return RLEIterator, assert_rle_iterator, run_rle_iterator


@app.cell
def _():
    # Example test case
    operations = ["RLEIterator", "next", "next", "next", "next"]
    inputs = [[3, 8, 0, 9, 2, 5], [2], [1], [1], [2]]
    expected = [None, 8, 8, 5, -1]
    return expected, inputs, operations


@app.cell
def _(RLEIterator, inputs, operations, run_rle_iterator):
    result, iterator = run_rle_iterator(RLEIterator, operations, inputs)
    print(result)
    iterator
    return (result,)


@app.cell
def _(assert_rle_iterator, expected, result):
    assert_rle_iterator(result, expected)
    return


if __name__ == "__main__":
    app.run()
