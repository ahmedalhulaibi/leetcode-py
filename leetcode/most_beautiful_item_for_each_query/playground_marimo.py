import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_beauty, run_maximum_beauty
    from solution import Solution

    return Solution, assert_maximum_beauty, run_maximum_beauty


@app.cell
def _():
    # Example test case
    items: list[list[int]] = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
    queries: list[int] = [1, 2, 3, 4, 5, 6]
    expected: list[int] = [2, 4, 5, 5, 6, 6]
    return expected, items, queries


@app.cell
def _(
    Solution,
    items: list[list[int]],
    queries: list[int],
    run_maximum_beauty,
):
    result = run_maximum_beauty(Solution, items, queries)
    result
    return (result,)


@app.cell
def _(assert_maximum_beauty, expected: list[int], result):
    assert_maximum_beauty(result, expected)
    return


if __name__ == "__main__":
    app.run()
