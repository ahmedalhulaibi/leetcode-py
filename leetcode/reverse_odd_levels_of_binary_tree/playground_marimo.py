import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reverse_odd_levels, run_reverse_odd_levels
    from solution import Solution

    return Solution, assert_reverse_odd_levels, run_reverse_odd_levels


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [2, 3, 5, 8, 13, 21, 34]
    expected_list: list[int | None] = [2, 5, 3, 8, 13, 21, 34]
    return expected_list, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_reverse_odd_levels):
    result = run_reverse_odd_levels(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_reverse_odd_levels, expected_list: list[int | None], result):
    assert_reverse_odd_levels(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
