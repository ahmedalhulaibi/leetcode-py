import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_magical_string, run_magical_string
    from solution import Solution

    return Solution, assert_magical_string, run_magical_string


@app.cell
def _():
    # Example test case
    n: int = 6
    expected: int = 3
    return expected, n


@app.cell
def _(Solution, n: int, run_magical_string):
    result = run_magical_string(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_magical_string, expected: int, result):
    assert_magical_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
