import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_smallest_from_leaf, run_smallest_from_leaf
    from solution import Solution

    return Solution, assert_smallest_from_leaf, run_smallest_from_leaf


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [0, 1, 2, 3, 4, 3, 4]
    expected = "dba"
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_smallest_from_leaf):
    result = run_smallest_from_leaf(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_smallest_from_leaf, expected, result):
    assert_smallest_from_leaf(result, expected)
    return


if __name__ == "__main__":
    app.run()
