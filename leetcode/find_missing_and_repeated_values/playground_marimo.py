import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_missing_and_repeated_values, run_find_missing_and_repeated_values
    from solution import Solution

    return (
        Solution,
        assert_find_missing_and_repeated_values,
        run_find_missing_and_repeated_values,
    )


@app.cell
def _():
    # Example test case
    grid: list[list[int]] = [[1, 3], [2, 2]]
    expected: list[int] = [2, 4]
    return expected, grid


@app.cell
def _(Solution, grid: list[list[int]], run_find_missing_and_repeated_values):
    result = run_find_missing_and_repeated_values(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_find_missing_and_repeated_values, expected: list[int], result):
    assert_find_missing_and_repeated_values(result, expected)
    return


if __name__ == "__main__":
    app.run()
