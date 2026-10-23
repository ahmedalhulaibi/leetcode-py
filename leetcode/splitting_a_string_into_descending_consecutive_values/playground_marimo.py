import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_split_string, run_split_string
    from solution import Solution

    return Solution, assert_split_string, run_split_string


@app.cell
def _():
    # Example test case
    s = "050043"
    expected = True
    return expected, s


@app.cell
def _(Solution, run_split_string, s):
    result = run_split_string(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_split_string, expected, result):
    assert_split_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
