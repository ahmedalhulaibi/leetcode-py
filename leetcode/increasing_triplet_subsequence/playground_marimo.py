import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_increasing_triplet, run_increasing_triplet
    from solution import Solution

    return Solution, assert_increasing_triplet, run_increasing_triplet


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 4, 5]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_increasing_triplet):
    result = run_increasing_triplet(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_increasing_triplet, expected, result):
    assert_increasing_triplet(result, expected)
    return


if __name__ == "__main__":
    app.run()
