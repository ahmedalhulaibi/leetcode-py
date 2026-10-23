import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_binary_search_tree_iterator, run_binary_search_tree_iterator
    from solution import BSTIterator

    return (
        BSTIterator,
        assert_binary_search_tree_iterator,
        run_binary_search_tree_iterator,
    )


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [7, 3, 15, None, None, 9, 20]
    operations = [
        "next",
        "next",
        "has_next",
        "next",
        "has_next",
        "next",
        "has_next",
        "next",
        "has_next",
    ]
    expected: list[int | bool | None] = [None, 3, 7, True, 9, True, 15, True, 20, False]
    return expected, operations, root_list


@app.cell
def _(
    BSTIterator,
    operations,
    root_list: list[int | None],
    run_binary_search_tree_iterator,
):
    result, iterator = run_binary_search_tree_iterator(BSTIterator, root_list, operations)
    print(result)
    iterator
    return (result,)


@app.cell
def _(
    assert_binary_search_tree_iterator,
    expected: list[int | bool | None],
    result,
):
    assert_binary_search_tree_iterator(result, expected)
    return


if __name__ == "__main__":
    app.run()
