import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_reach, run_can_reach
    from solution import Solution

    return Solution, assert_can_reach, run_can_reach


@app.cell
def _():
    # Example test case
    s = "011010"
    min_jump = 2
    max_jump = 3
    expected = True
    return expected, max_jump, min_jump, s


@app.cell
def _(Solution, max_jump, min_jump, run_can_reach, s):
    result = run_can_reach(Solution, s, min_jump, max_jump)
    result
    return (result,)


@app.cell
def _(assert_can_reach, expected, result):
    assert_can_reach(result, expected)
    return


if __name__ == "__main__":
    app.run()
