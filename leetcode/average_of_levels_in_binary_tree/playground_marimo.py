import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_average_of_levels, run_average_of_levels
    from solution import Solution

    return Solution, assert_average_of_levels, run_average_of_levels


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
    expected = [3.0, 14.5, 11.0]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_average_of_levels):
    result = run_average_of_levels(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_average_of_levels, expected, result):
    assert_average_of_levels(result, expected)
    return


if __name__ == "__main__":
    app.run()
