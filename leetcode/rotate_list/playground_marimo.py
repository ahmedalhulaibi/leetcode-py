import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rotate_right, run_rotate_right
    from solution import Solution

    return Solution, assert_rotate_right, run_rotate_right


@app.cell
def _():
    # Example test case
    head_list = [1, 2, 3, 4, 5]
    k = 2
    expected = [4, 5, 1, 2, 3]
    return expected, head_list, k


@app.cell
def _(Solution, head_list, k, run_rotate_right):
    result = run_rotate_right(Solution, head_list, k)
    result
    return (result,)


@app.cell
def _(assert_rotate_right, expected, result):
    assert_rotate_right(result, expected)
    return


if __name__ == "__main__":
    app.run()
