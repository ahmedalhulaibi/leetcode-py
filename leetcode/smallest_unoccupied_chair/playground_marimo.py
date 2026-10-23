import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_smallest_chair, run_smallest_chair
    from solution import Solution

    return Solution, assert_smallest_chair, run_smallest_chair


@app.cell
def _():
    # Example test case
    times = [[1, 4], [2, 3], [4, 6]]
    target_friend = 1
    expected = 1
    return expected, target_friend, times


@app.cell
def _(Solution, run_smallest_chair, target_friend, times):
    result = run_smallest_chair(Solution, times, target_friend)
    result
    return (result,)


@app.cell
def _(assert_smallest_chair, expected, result):
    assert_smallest_chair(result, expected)
    return


if __name__ == "__main__":
    app.run()
