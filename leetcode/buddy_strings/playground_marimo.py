import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_buddy_strings, run_buddy_strings
    from solution import Solution

    return Solution, assert_buddy_strings, run_buddy_strings


@app.cell
def _():
    # Example test case
    s = "ab"
    goal = "ba"
    expected = True
    return expected, goal, s


@app.cell
def _(Solution, goal, run_buddy_strings, s):
    result = run_buddy_strings(Solution, s, goal)
    result
    return (result,)


@app.cell
def _(assert_buddy_strings, expected, result):
    assert_buddy_strings(result, expected)
    return


if __name__ == "__main__":
    app.run()
