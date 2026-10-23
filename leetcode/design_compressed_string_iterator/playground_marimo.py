import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_string_iterator, run_string_iterator
    from solution import StringIterator

    return StringIterator, assert_string_iterator, run_string_iterator


@app.cell
def _():
    # Example test case
    operations = ["StringIterator", "next", "next", "has_next"]
    inputs = [["L1e2t1C1o1d1e1"], [], [], []]
    expected = [None, "L", "e", True]
    return expected, inputs, operations


@app.cell
def _(StringIterator, inputs, operations, run_string_iterator):
    result, iterator = run_string_iterator(StringIterator, operations, inputs)
    print(result)
    iterator
    return (result,)


@app.cell
def _(assert_string_iterator, expected, result):
    assert_string_iterator(result, expected)
    return


if __name__ == "__main__":
    app.run()
