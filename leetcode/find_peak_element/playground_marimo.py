import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_peak_element, run_find_peak_element
    from solution import Solution

    return Solution, assert_find_peak_element, run_find_peak_element


@app.cell
def _():
    # Example test case
    nums: list[int] = [1, 2, 3, 1]
    expected: int = 2
    return expected, nums


@app.cell
def _(Solution, nums: list[int], run_find_peak_element):
    result = run_find_peak_element(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_peak_element, expected: int, result):
    assert_find_peak_element(result, expected)
    return


if __name__ == "__main__":
    app.run()
