import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_level_order_bottom, run_level_order_bottom
    from solution import Solution

    return Solution, assert_level_order_bottom, run_level_order_bottom


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
    expected = [[15, 7], [9, 20], [3]]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_level_order_bottom):
    result = run_level_order_bottom(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_level_order_bottom, expected, result):
    assert_level_order_bottom(result, expected)
    return


if __name__ == "__main__":
    app.run()
