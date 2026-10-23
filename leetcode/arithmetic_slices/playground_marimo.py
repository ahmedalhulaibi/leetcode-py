import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_number_of_arithmetic_slices, run_number_of_arithmetic_slices
    from solution import Solution

    return (
        Solution,
        assert_number_of_arithmetic_slices,
        run_number_of_arithmetic_slices,
    )


@app.cell
def _():
    # Example test case
    nums: list[int] = [1, 2, 3, 4]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums: list[int], run_number_of_arithmetic_slices):
    result = run_number_of_arithmetic_slices(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_number_of_arithmetic_slices, expected, result):
    assert_number_of_arithmetic_slices(result, expected)
    return


if __name__ == "__main__":
    app.run()
