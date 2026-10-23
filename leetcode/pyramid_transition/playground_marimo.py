import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_pyramid_transition, run_pyramid_transition
    from solution import Solution

    return Solution, assert_pyramid_transition, run_pyramid_transition


@app.cell
def _():
    # Example test case
    bottom = "BCD"
    allowed = ["BCC", "CDE", "CEA", "FFF"]
    expected = True
    return allowed, bottom, expected


@app.cell
def _(Solution, allowed, bottom, run_pyramid_transition):
    result = run_pyramid_transition(Solution, bottom, allowed)
    result
    return (result,)


@app.cell
def _(assert_pyramid_transition, expected, result):
    assert_pyramid_transition(result, expected)
    return


if __name__ == "__main__":
    app.run()
