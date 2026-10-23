import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_ideal_string, run_longest_ideal_string
    from solution import Solution

    return Solution, assert_longest_ideal_string, run_longest_ideal_string


@app.cell
def _():
    # Example test case
    s = "acfgbd"
    k = 2
    expected = 4
    return expected, k, s


@app.cell
def _(Solution, k, run_longest_ideal_string, s):
    result = run_longest_ideal_string(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_longest_ideal_string, expected, result):
    assert_longest_ideal_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
