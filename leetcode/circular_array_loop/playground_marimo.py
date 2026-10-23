import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_circular_array_loop, run_circular_array_loop
    from solution import Solution

    return Solution, assert_circular_array_loop, run_circular_array_loop


@app.cell
def _():
    # Example test case
    nums = [2, -1, 1, 2, 2]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_circular_array_loop):
    result = run_circular_array_loop(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_circular_array_loop, expected, result):
    assert_circular_array_loop(result, expected)
    return


if __name__ == "__main__":
    app.run()
