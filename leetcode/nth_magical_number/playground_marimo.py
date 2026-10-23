import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_nth_magical_number, run_nth_magical_number
    from solution import Solution

    return Solution, assert_nth_magical_number, run_nth_magical_number


@app.cell
def _():
    # Example test case
    n = 4
    a = 2
    b = 3
    expected = 6
    return a, b, expected, n


@app.cell
def _(Solution, a, b, n, run_nth_magical_number):
    result = run_nth_magical_number(Solution, n, a, b)
    result
    return (result,)


@app.cell
def _(assert_nth_magical_number, expected, result):
    assert_nth_magical_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
