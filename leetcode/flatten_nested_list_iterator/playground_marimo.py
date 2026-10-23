import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_flatten_nested_list_iterator, run_flatten_nested_list_iterator
    from solution import NestedIterator

    return (
        NestedIterator,
        assert_flatten_nested_list_iterator,
        run_flatten_nested_list_iterator,
    )


@app.cell
def _():
    # Example test case
    nested_list = [[1, 1], 2, [1, 1]]
    expected = [1, 1, 2, 1, 1]
    return expected, nested_list


@app.cell
def _(NestedIterator, nested_list, run_flatten_nested_list_iterator):
    result = run_flatten_nested_list_iterator(NestedIterator, nested_list)
    result
    return (result,)


@app.cell
def _(assert_flatten_nested_list_iterator, expected, result):
    assert_flatten_nested_list_iterator(result, expected)
    return


if __name__ == "__main__":
    app.run()
