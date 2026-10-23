import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rotate_string, run_rotate_string
    from solution import Solution

    return Solution, assert_rotate_string, run_rotate_string


@app.cell
def _():
    # Example test case
    s = "abcde"
    goal = "cdeab"
    expected = True
    return expected, goal, s


@app.cell
def _(Solution, goal, run_rotate_string, s):
    result = run_rotate_string(Solution, s, goal)
    result
    return (result,)


@app.cell
def _(assert_rotate_string, expected, result):
    assert_rotate_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
