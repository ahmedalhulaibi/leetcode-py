import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_be_valid, run_can_be_valid
    from solution import Solution

    return Solution, assert_can_be_valid, run_can_be_valid


@app.cell
def _():
    # Example test case
    s = "))()))"
    locked = "010100"
    expected = True
    return expected, locked, s


@app.cell
def _(Solution, locked, run_can_be_valid, s):
    result = run_can_be_valid(Solution, s, locked)
    result
    return (result,)


@app.cell
def _(assert_can_be_valid, expected, result):
    assert_can_be_valid(result, expected)
    return


if __name__ == "__main__":
    app.run()
