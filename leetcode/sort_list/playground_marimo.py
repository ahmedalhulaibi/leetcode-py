import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sort_list, run_sort_list
    from solution import Solution

    return Solution, assert_sort_list, run_sort_list


@app.cell
def _():
    # Example test case
    head_list = [4, 2, 1, 3]
    expected = [1, 2, 3, 4]
    return expected, head_list


@app.cell
def _(Solution, head_list, run_sort_list):
    result = run_sort_list(Solution, head_list)
    result
    return (result,)


@app.cell
def _(assert_sort_list, expected, result):
    assert_sort_list(result, expected)
    return


if __name__ == "__main__":
    app.run()
