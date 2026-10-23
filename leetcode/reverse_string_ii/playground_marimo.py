import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reverse_str, run_reverse_str
    from solution import Solution

    return Solution, assert_reverse_str, run_reverse_str


@app.cell
def _():
    # Example test case
    s = "abcdefg"
    k = 2
    expected = "bacdfeg"
    return expected, k, s


@app.cell
def _(Solution, k, run_reverse_str, s):
    result = run_reverse_str(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_reverse_str, expected, result):
    assert_reverse_str(result, expected)
    return


if __name__ == "__main__":
    app.run()
