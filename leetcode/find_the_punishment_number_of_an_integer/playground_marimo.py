import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_punishment_number, run_punishment_number
    from solution import Solution

    return Solution, assert_punishment_number, run_punishment_number


@app.cell
def _():
    # Example test case
    n = 10
    expected = 182
    return expected, n


@app.cell
def _(Solution, n, run_punishment_number):
    result = run_punishment_number(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_punishment_number, expected, result):
    assert_punishment_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
