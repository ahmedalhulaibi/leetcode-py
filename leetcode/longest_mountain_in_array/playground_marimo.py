import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_mountain, run_longest_mountain
    from solution import Solution

    return Solution, assert_longest_mountain, run_longest_mountain


@app.cell
def _():
    # Example test case
    arr: list[int] = [2, 1, 4, 7, 3, 2, 5]
    expected: int = 5
    return arr, expected


@app.cell
def _(Solution, arr: list[int], run_longest_mountain):
    result = run_longest_mountain(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_longest_mountain, expected: int, result):
    assert_longest_mountain(result, expected)
    return


if __name__ == "__main__":
    app.run()
