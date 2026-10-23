import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_unique_split, run_max_unique_split
    from solution import Solution

    return Solution, assert_max_unique_split, run_max_unique_split


@app.cell
def _():
    # Example test case
    s = "ababccc"
    expected = 5
    return expected, s


@app.cell
def _(Solution, run_max_unique_split, s):
    result = run_max_unique_split(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_max_unique_split, expected, result):
    assert_max_unique_split(result, expected)
    return


if __name__ == "__main__":
    app.run()
