import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_number_of_arrays, run_number_of_arrays
    from solution import Solution

    return Solution, assert_number_of_arrays, run_number_of_arrays


@app.cell
def _():
    # Example test case
    differences = [1, -3, 4]
    lower = 1
    upper = 6
    expected = 2
    return differences, expected, lower, upper


@app.cell
def _(Solution, differences, lower, run_number_of_arrays, upper):
    result = run_number_of_arrays(Solution, differences, lower, upper)
    result
    return (result,)


@app.cell
def _(assert_number_of_arrays, expected, result):
    assert_number_of_arrays(result, expected)
    return


if __name__ == "__main__":
    app.run()
