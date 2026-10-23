import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_split_looping_string, run_split_looping_string
    from solution import Solution

    return Solution, assert_split_looping_string, run_split_looping_string


@app.cell
def _():
    # Example test case
    strs = ["abc", "xyz"]
    expected = "zyxcba"
    return expected, strs


@app.cell
def _(Solution, run_split_looping_string, strs):
    result = run_split_looping_string(Solution, strs)
    result
    return (result,)


@app.cell
def _(assert_split_looping_string, expected, result):
    assert_split_looping_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
