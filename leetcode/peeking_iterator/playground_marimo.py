import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_peeking_iterator, run_peeking_iterator
    from solution import PeekingIterator

    return PeekingIterator, assert_peeking_iterator, run_peeking_iterator


@app.cell
def _():
    # Example test case
    operations = ["PeekingIterator", "next", "peek", "next", "next", "has_next"]
    inputs = [[[1, 2, 3]], [], [], [], [], []]
    expected = [None, 1, 2, 2, 3, False]
    return expected, inputs, operations


@app.cell
def _(PeekingIterator, inputs, operations, run_peeking_iterator):
    result, iterator = run_peeking_iterator(PeekingIterator, operations, inputs)
    print(result)
    iterator
    return (result,)


@app.cell
def _(assert_peeking_iterator, expected, result):
    assert_peeking_iterator(result, expected)
    return


if __name__ == "__main__":
    app.run()
