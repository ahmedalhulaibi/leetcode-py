import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_odd_even_jumps, run_odd_even_jumps
    from solution import Solution

    return Solution, assert_odd_even_jumps, run_odd_even_jumps


@app.cell
def _():
    # Example test case
    arr = [10, 13, 12, 14, 15]
    expected = 2
    return arr, expected


@app.cell
def _(Solution, arr, run_odd_even_jumps):
    result = run_odd_even_jumps(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_odd_even_jumps, expected, result):
    assert_odd_even_jumps(result, expected)
    return


if __name__ == "__main__":
    app.run()
