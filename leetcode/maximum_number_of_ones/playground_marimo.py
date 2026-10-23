import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_number_of_ones, run_maximum_number_of_ones
    from solution import Solution

    return Solution, assert_maximum_number_of_ones, run_maximum_number_of_ones


@app.cell
def _():
    # Example test case
    width = 3
    height = 3
    side_length = 2
    max_ones = 1
    expected = 4
    return expected, height, max_ones, side_length, width


@app.cell
def _(
    Solution,
    height,
    max_ones,
    run_maximum_number_of_ones,
    side_length,
    width,
):
    result = run_maximum_number_of_ones(Solution, width, height, side_length, max_ones)
    result
    return (result,)


@app.cell
def _(assert_maximum_number_of_ones, expected, result):
    assert_maximum_number_of_ones(result, expected)
    return


if __name__ == "__main__":
    app.run()
