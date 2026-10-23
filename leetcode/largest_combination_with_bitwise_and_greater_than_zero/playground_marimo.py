import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_combination, run_largest_combination
    from solution import Solution

    return Solution, assert_largest_combination, run_largest_combination


@app.cell
def _():
    # Example test case
    candidates = [16, 17, 71, 62, 12, 24, 14]
    expected = 4
    return candidates, expected


@app.cell
def _(Solution, candidates, run_largest_combination):
    result = run_largest_combination(Solution, candidates)
    result
    return (result,)


@app.cell
def _(assert_largest_combination, expected, result):
    assert_largest_combination(result, expected)
    return


if __name__ == "__main__":
    app.run()
