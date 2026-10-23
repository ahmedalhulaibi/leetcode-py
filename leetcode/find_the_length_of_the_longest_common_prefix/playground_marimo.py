import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_common_prefix, run_longest_common_prefix
    from solution import Solution

    return Solution, assert_longest_common_prefix, run_longest_common_prefix


@app.cell
def _():
    # Example test case
    arr1: list[int] = [1, 10, 100]
    arr2: list[int] = [1000]
    expected = 3
    return arr1, arr2, expected


@app.cell
def _(Solution, arr1: list[int], arr2: list[int], run_longest_common_prefix):
    result = run_longest_common_prefix(Solution, arr1, arr2)
    result
    return (result,)


@app.cell
def _(assert_longest_common_prefix, expected, result):
    assert_longest_common_prefix(result, expected)
    return


if __name__ == "__main__":
    app.run()
