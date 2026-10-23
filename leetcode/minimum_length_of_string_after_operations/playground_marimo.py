import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_length, run_minimum_length
    from solution import Solution

    return Solution, assert_minimum_length, run_minimum_length


@app.cell
def _():
    # Example test case
    s = "abaacbcbb"
    expected = 5
    return expected, s


@app.cell
def _(Solution, run_minimum_length, s):
    result = run_minimum_length(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_minimum_length, expected, result):
    assert_minimum_length(result, expected)
    return


if __name__ == "__main__":
    app.run()
