import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_stepping_numbers, run_count_stepping_numbers
    from solution import Solution

    return Solution, assert_count_stepping_numbers, run_count_stepping_numbers


@app.cell
def _():
    # Example test case
    low: int = 0
    high: int = 21
    expected: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]
    return expected, high, low


@app.cell
def _(Solution, high: int, low: int, run_count_stepping_numbers):
    result = run_count_stepping_numbers(Solution, low, high)
    result
    return (result,)


@app.cell
def _(assert_count_stepping_numbers, expected: list[int], result):
    assert_count_stepping_numbers(result, expected)
    return


if __name__ == "__main__":
    app.run()
