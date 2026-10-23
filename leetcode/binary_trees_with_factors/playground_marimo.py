import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_factored_binary_trees, run_num_factored_binary_trees
    from solution import Solution

    return (
        Solution,
        assert_num_factored_binary_trees,
        run_num_factored_binary_trees,
    )


@app.cell
def _():
    # Example test case
    arr = [2, 4]
    expected = 3
    return arr, expected


@app.cell
def _(Solution, arr, run_num_factored_binary_trees):
    result = run_num_factored_binary_trees(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_num_factored_binary_trees, expected, result):
    assert_num_factored_binary_trees(result, expected)
    return


if __name__ == "__main__":
    app.run()
