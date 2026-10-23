import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_length, run_max_length
    from solution import Solution

    return Solution, assert_max_length, run_max_length


@app.cell
def _():
    # Example test case
    ribbons = [9, 7, 5]
    k = 3
    expected = 5
    return expected, k, ribbons


@app.cell
def _(Solution, k, ribbons, run_max_length):
    result = run_max_length(Solution, ribbons, k)
    result
    return (result,)


@app.cell
def _(assert_max_length, expected, result):
    assert_max_length(result, expected)
    return


if __name__ == "__main__":
    app.run()
