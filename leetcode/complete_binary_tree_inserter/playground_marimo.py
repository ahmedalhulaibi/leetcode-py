import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_complete_binary_tree_inserter, run_complete_binary_tree_inserter
    from solution import CBTInserter

    return (
        CBTInserter,
        assert_complete_binary_tree_inserter,
        run_complete_binary_tree_inserter,
    )


@app.cell
def _():
    # Example test case
    operations = ["CBTInserter", "insert", "insert", "get_root"]
    inputs = [[1, 2], [3], [4], []]
    expected: list[int | list[int | None] | None] = [None, 1, 2, [1, 2, 3, 4]]
    return expected, inputs, operations


@app.cell
def _(CBTInserter, inputs, operations, run_complete_binary_tree_inserter):
    result, inserter = run_complete_binary_tree_inserter(CBTInserter, operations, inputs)
    print(result)
    inserter
    return (result,)


@app.cell
def _(
    assert_complete_binary_tree_inserter,
    expected: list[int | list[int | None] | None],
    result,
):
    assert_complete_binary_tree_inserter(result, expected)
    return


if __name__ == "__main__":
    app.run()
