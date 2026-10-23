import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_invitations, run_maximum_invitations
    from solution import Solution

    return Solution, assert_maximum_invitations, run_maximum_invitations


@app.cell
def _():
    # Example test case
    favorite = [3, 0, 1, 4, 1]
    expected = 4
    return expected, favorite


@app.cell
def _(Solution, favorite, run_maximum_invitations):
    result = run_maximum_invitations(Solution, favorite)
    result
    return (result,)


@app.cell
def _(assert_maximum_invitations, expected, result):
    assert_maximum_invitations(result, expected)
    return


if __name__ == "__main__":
    app.run()
