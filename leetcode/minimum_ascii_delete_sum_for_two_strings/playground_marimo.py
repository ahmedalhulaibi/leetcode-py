import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_delete_sum, run_minimum_delete_sum
    from solution import Solution

    return Solution, assert_minimum_delete_sum, run_minimum_delete_sum


@app.cell
def _():
    # Example test case
    s1 = "sea"
    s2 = "eat"
    expected = 231
    return expected, s1, s2


@app.cell
def _(Solution, run_minimum_delete_sum, s1, s2):
    result = run_minimum_delete_sum(Solution, s1, s2)
    result
    return (result,)


@app.cell
def _(assert_minimum_delete_sum, expected, result):
    assert_minimum_delete_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
