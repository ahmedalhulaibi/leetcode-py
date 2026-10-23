import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reverse_string, run_reverse_string
    from solution import Solution

    return Solution, assert_reverse_string, run_reverse_string


@app.cell
def _():
    # Example test case
    s = ["h", "e", "l", "l", "o"]
    expected = ["o", "l", "l", "e", "h"]
    return expected, s


@app.cell
def _(Solution, run_reverse_string, s):
    result = run_reverse_string(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_reverse_string, expected, result):
    assert_reverse_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
