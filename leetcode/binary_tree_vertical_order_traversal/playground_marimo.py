import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_vertical_order, run_vertical_order
    from solution import Solution

    return Solution, assert_vertical_order, run_vertical_order


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
    expected = [[9], [3, 15], [20], [7]]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_vertical_order):
    result = run_vertical_order(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_vertical_order, expected, result):
    assert_vertical_order(result, expected)
    return


if __name__ == "__main__":
    app.run()
