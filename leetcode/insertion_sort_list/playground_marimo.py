import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_insertion_sort_list, run_insertion_sort_list
    from solution import Solution

    return Solution, assert_insertion_sort_list, run_insertion_sort_list


@app.cell
def _():
    # Example test case
    head_vals: list[int] = [4, 2, 1, 3]
    expected_vals: list[int] = [1, 2, 3, 4]
    return expected_vals, head_vals


@app.cell
def _(Solution, head_vals: list[int], run_insertion_sort_list):
    result = run_insertion_sort_list(Solution, head_vals)
    result
    return (result,)


@app.cell
def _(assert_insertion_sort_list, expected_vals: list[int], result):
    assert_insertion_sort_list(result, expected_vals)
    return


if __name__ == "__main__":
    app.run()
