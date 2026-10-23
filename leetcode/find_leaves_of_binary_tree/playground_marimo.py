import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_leaves, run_find_leaves
    from solution import Solution

    return Solution, assert_find_leaves, run_find_leaves


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3, 4, 5]
    expected: list[list[int]] = [[4, 5, 3], [2], [1]]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_find_leaves):
    result = run_find_leaves(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_find_leaves, expected: list[list[int]], result):
    assert_find_leaves(result, expected)
    return


if __name__ == "__main__":
    app.run()
