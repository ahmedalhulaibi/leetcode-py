import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_pick_gifts, run_pick_gifts
    from solution import Solution

    return Solution, assert_pick_gifts, run_pick_gifts


@app.cell
def _():
    # Example test case
    gifts = [25, 64, 9, 4, 100]
    k = 4
    expected = 29
    return expected, gifts, k


@app.cell
def _(Solution, gifts, k, run_pick_gifts):
    result = run_pick_gifts(Solution, gifts, k)
    result
    return (result,)


@app.cell
def _(assert_pick_gifts, expected, result):
    assert_pick_gifts(result, expected)
    return


if __name__ == "__main__":
    app.run()
