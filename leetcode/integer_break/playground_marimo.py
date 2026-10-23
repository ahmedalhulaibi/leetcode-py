import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_integer_break, run_integer_break
    from solution import Solution

    return Solution, assert_integer_break, run_integer_break


@app.cell
def _():
    # Example test case
    n = 10
    expected = 36
    return expected, n


@app.cell
def _(Solution, n, run_integer_break):
    result = run_integer_break(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_integer_break, expected, result):
    assert_integer_break(result, expected)
    return


if __name__ == "__main__":
    app.run()
