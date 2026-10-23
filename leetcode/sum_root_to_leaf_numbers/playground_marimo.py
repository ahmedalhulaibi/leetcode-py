import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sum_numbers, run_sum_numbers
    from solution import Solution

    return Solution, assert_sum_numbers, run_sum_numbers


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [4, 9, 0, 5, 1]
    expected: int = 1026
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_sum_numbers):
    result = run_sum_numbers(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_sum_numbers, expected: int, result):
    assert_sum_numbers(result, expected)
    return


if __name__ == "__main__":
    app.run()
