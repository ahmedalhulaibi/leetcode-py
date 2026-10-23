import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_dominant_index, run_dominant_index
    from solution import Solution

    return Solution, assert_dominant_index, run_dominant_index


@app.cell
def _():
    # Example test case
    nums = [3, 6, 1, 0]
    expected = 1
    return expected, nums


@app.cell
def _(Solution, nums, run_dominant_index):
    result = run_dominant_index(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_dominant_index, expected, result):
    assert_dominant_index(result, expected)
    return


if __name__ == "__main__":
    app.run()
