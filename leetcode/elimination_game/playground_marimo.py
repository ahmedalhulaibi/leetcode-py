import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_last_remaining, run_last_remaining
    from solution import Solution

    return Solution, assert_last_remaining, run_last_remaining


@app.cell
def _():
    # Example test case
    n: int = 9
    expected: int = 6
    return expected, n


@app.cell
def _(Solution, n: int, run_last_remaining):
    result = run_last_remaining(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_last_remaining, expected: int, result):
    assert_last_remaining(result, expected)
    return


if __name__ == "__main__":
    app.run()
