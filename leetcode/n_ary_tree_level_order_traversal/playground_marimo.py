import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_level_order, run_level_order
    from solution import Solution

    return Solution, assert_level_order, run_level_order


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, None, 3, 2, 4, None, 5, 6]
    expected = [[1], [3, 2, 4], [5, 6]]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_level_order):
    result = run_level_order(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_level_order, expected, result):
    assert_level_order(result, expected)
    return


if __name__ == "__main__":
    app.run()
