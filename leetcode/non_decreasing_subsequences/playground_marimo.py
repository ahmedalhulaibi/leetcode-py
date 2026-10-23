import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_subsequences, run_find_subsequences
    from solution import Solution

    return Solution, assert_find_subsequences, run_find_subsequences


@app.cell
def _():
    # Example test case
    nums = [4, 6, 7, 7]
    expected = [
        [4, 6],
        [4, 6, 7],
        [4, 6, 7, 7],
        [4, 7],
        [4, 7, 7],
        [6, 7],
        [6, 7, 7],
        [7, 7],
    ]
    return expected, nums


@app.cell
def _(Solution, nums, run_find_subsequences):
    result = run_find_subsequences(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_subsequences, expected, result):
    assert_find_subsequences(result, expected)
    return


if __name__ == "__main__":
    app.run()
