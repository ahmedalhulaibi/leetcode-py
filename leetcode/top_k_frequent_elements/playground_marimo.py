import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_top_k_frequent, run_top_k_frequent
    from solution import Solution

    return Solution, assert_top_k_frequent, run_top_k_frequent


@app.cell
def _():
    # Example test case
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    expected = [1, 2]
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_top_k_frequent):
    result = run_top_k_frequent(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_top_k_frequent, expected, result):
    assert_top_k_frequent(result, expected)
    return


if __name__ == "__main__":
    app.run()
