import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_trim_bst, run_trim_bst
    from solution import Solution

    return Solution, assert_trim_bst, run_trim_bst


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 0, 2]
    low = 1
    high = 2
    expected_list: list[int | None] = [1, None, 2]
    return expected_list, high, low, root_list


@app.cell
def _(Solution, high, low, root_list: list[int | None], run_trim_bst):
    result = run_trim_bst(Solution, root_list, low, high)
    result
    return (result,)


@app.cell
def _(assert_trim_bst, expected_list: list[int | None], result):
    assert_trim_bst(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
