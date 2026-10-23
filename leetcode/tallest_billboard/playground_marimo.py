import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_tallest_billboard, run_tallest_billboard
    from solution import Solution

    return Solution, assert_tallest_billboard, run_tallest_billboard


@app.cell
def _():
    # Example test case
    rods = [1, 2, 3, 6]
    expected = 6
    return expected, rods


@app.cell
def _(Solution, rods, run_tallest_billboard):
    result = run_tallest_billboard(Solution, rods)
    result
    return (result,)


@app.cell
def _(assert_tallest_billboard, expected, result):
    assert_tallest_billboard(result, expected)
    return


if __name__ == "__main__":
    app.run()
