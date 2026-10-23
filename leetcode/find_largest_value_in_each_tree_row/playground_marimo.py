import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_values, run_largest_values
    from solution import Solution

    return Solution, assert_largest_values, run_largest_values


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 3, 2, 5, 3, None, 9]
    expected = [1, 3, 9]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_largest_values):
    result = run_largest_values(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_largest_values, expected, result):
    assert_largest_values(result, expected)
    return


if __name__ == "__main__":
    app.run()
