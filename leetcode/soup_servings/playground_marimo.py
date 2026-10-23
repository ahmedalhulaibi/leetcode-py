import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_soup_servings, run_soup_servings
    from solution import Solution

    return Solution, assert_soup_servings, run_soup_servings


@app.cell
def _():
    # Example test case
    n = 50
    expected = 0.625
    return expected, n


@app.cell
def _(Solution, n, run_soup_servings):
    result = run_soup_servings(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_soup_servings, expected, result):
    assert_soup_servings(result, expected)
    return


if __name__ == "__main__":
    app.run()
