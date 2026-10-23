import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_repeated_n_times, run_repeated_n_times
    from solution import Solution

    return Solution, assert_repeated_n_times, run_repeated_n_times


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 3]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums, run_repeated_n_times):
    result = run_repeated_n_times(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_repeated_n_times, expected, result):
    assert_repeated_n_times(result, expected)
    return


if __name__ == "__main__":
    app.run()
