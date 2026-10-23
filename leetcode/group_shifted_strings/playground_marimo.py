import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_group_strings, run_group_strings
    from solution import Solution

    return Solution, assert_group_strings, run_group_strings


@app.cell
def _():
    # Example test case
    strings = ["abc", "bcd"]
    expected = [["abc", "bcd"]]
    return expected, strings


@app.cell
def _(Solution, run_group_strings, strings):
    result = run_group_strings(Solution, strings)
    result
    return (result,)


@app.cell
def _(assert_group_strings, expected, result):
    assert_group_strings(result, expected)
    return


if __name__ == "__main__":
    app.run()
