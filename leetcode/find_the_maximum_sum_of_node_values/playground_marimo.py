import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_value_sum, run_maximum_value_sum
    from solution import Solution

    return Solution, assert_maximum_value_sum, run_maximum_value_sum


@app.cell
def _():
    # Example test case
    nums = [1, 2, 1]
    k = 3
    edges = [[0, 1], [0, 2]]
    expected = 6
    return edges, expected, k, nums


@app.cell
def _(Solution, edges, k, nums, run_maximum_value_sum):
    result = run_maximum_value_sum(Solution, nums, k, edges)
    result
    return (result,)


@app.cell
def _(assert_maximum_value_sum, expected, result):
    assert_maximum_value_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
