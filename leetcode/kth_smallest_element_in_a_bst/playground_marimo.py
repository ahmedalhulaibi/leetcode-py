import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_kth_smallest, run_kth_smallest
    from solution import Solution

    return Solution, assert_kth_smallest, run_kth_smallest


@app.cell
def _():
    # Example test case
    root_list = [3, 1, 4, None, 2]
    k = 1
    expected = 1
    return expected, k, root_list


@app.cell
def _(Solution, k, root_list, run_kth_smallest):
    result = run_kth_smallest(Solution, root_list, k)
    result
    return (result,)


@app.cell
def _(assert_kth_smallest, expected, result):
    assert_kth_smallest(result, expected)
    return


if __name__ == "__main__":
    app.run()
