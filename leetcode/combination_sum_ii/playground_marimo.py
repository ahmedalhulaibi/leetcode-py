import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_combination_sum2, run_combination_sum2
    from solution import Solution

    return Solution, assert_combination_sum2, run_combination_sum2


@app.cell
def _():
    # Example test case
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    return candidates, expected, target


@app.cell
def _(Solution, candidates, run_combination_sum2, target):
    result = run_combination_sum2(Solution, candidates, target)
    result
    return (result,)


@app.cell
def _(assert_combination_sum2, expected, result):
    assert_combination_sum2(result, expected)
    return


if __name__ == "__main__":
    app.run()
