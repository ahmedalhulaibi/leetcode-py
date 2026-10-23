import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_minimum_difference, run_get_minimum_difference
    from solution import Solution

    return Solution, assert_get_minimum_difference, run_get_minimum_difference


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [4, 2, 6, 1, 3]
    expected = 1
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_get_minimum_difference):
    result = run_get_minimum_difference(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_get_minimum_difference, expected, result):
    assert_get_minimum_difference(result, expected)
    return


if __name__ == "__main__":
    app.run()
