import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_divide_into_subsequences, run_can_divide_into_subsequences
    from solution import Solution

    return (
        Solution,
        assert_can_divide_into_subsequences,
        run_can_divide_into_subsequences,
    )


@app.cell
def _():
    # Example test case
    nums = [1, 2, 2, 3, 3, 4, 4]
    k = 3
    expected = True
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_can_divide_into_subsequences):
    result = run_can_divide_into_subsequences(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_can_divide_into_subsequences, expected, result):
    assert_can_divide_into_subsequences(result, expected)
    return


if __name__ == "__main__":
    app.run()
