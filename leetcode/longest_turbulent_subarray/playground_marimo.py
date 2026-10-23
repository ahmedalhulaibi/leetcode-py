import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_turbulence_size, run_max_turbulence_size
    from solution import Solution

    return Solution, assert_max_turbulence_size, run_max_turbulence_size


@app.cell
def _():
    # Example test case
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    expected = 5
    return arr, expected


@app.cell
def _(Solution, arr, run_max_turbulence_size):
    result = run_max_turbulence_size(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_max_turbulence_size, expected, result):
    assert_max_turbulence_size(result, expected)
    return


if __name__ == "__main__":
    app.run()
