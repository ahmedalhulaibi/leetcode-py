import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_combination_sum, run_combination_sum
    from solution import Solution

    return Solution, assert_combination_sum, run_combination_sum


@app.cell
def _():
    # Example test case
    candidates = [2, 3, 6, 7]
    target = 7
    expected = [[2, 2, 3], [7]]
    return candidates, expected, target


@app.cell
def _(Solution, candidates, run_combination_sum, target):
    result = run_combination_sum(Solution, candidates, target)
    result
    return (result,)


@app.cell
def _(assert_combination_sum, expected, result):
    assert_combination_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
