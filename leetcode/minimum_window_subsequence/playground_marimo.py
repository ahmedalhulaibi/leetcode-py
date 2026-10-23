import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_window, run_min_window
    from solution import Solution

    return Solution, assert_min_window, run_min_window


@app.cell
def _():
    # Example test case
    s1 = "abcdebdde"
    s2 = "bde"
    expected = "bcde"
    return expected, s1, s2


@app.cell
def _(Solution, run_min_window, s1, s2):
    result = run_min_window(Solution, s1, s2)
    result
    return (result,)


@app.cell
def _(assert_min_window, expected, result):
    assert_min_window(result, expected)
    return


if __name__ == "__main__":
    app.run()
