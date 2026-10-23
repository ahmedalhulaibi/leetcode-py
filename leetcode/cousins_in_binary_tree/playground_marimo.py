import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_cousins, run_is_cousins
    from solution import Solution

    return Solution, assert_is_cousins, run_is_cousins


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3, 4]
    x = 4
    y = 3
    expected = False
    return expected, root_list, x, y


@app.cell
def _(Solution, root_list: list[int | None], run_is_cousins, x, y):
    result = run_is_cousins(Solution, root_list, x, y)
    result
    return (result,)


@app.cell
def _(assert_is_cousins, expected, result):
    assert_is_cousins(result, expected)
    return


if __name__ == "__main__":
    app.run()
