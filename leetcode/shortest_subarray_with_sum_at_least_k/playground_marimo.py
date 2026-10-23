import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_subarray, run_shortest_subarray
    from solution import Solution

    return Solution, assert_shortest_subarray, run_shortest_subarray


@app.cell
def _():
    # Example test case
    nums = [2, -1, 2]
    k = 3
    expected = 3
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_shortest_subarray):
    result = run_shortest_subarray(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_shortest_subarray, expected, result):
    assert_shortest_subarray(result, expected)
    return


if __name__ == "__main__":
    app.run()
