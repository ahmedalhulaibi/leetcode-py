import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_circle_num, run_find_circle_num
    from solution import Solution

    return Solution, assert_find_circle_num, run_find_circle_num


@app.cell
def _():
    # Example test case
    is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    expected = 2
    return expected, is_connected


@app.cell
def _(Solution, is_connected, run_find_circle_num):
    result = run_find_circle_num(Solution, is_connected)
    result
    return (result,)


@app.cell
def _(assert_find_circle_num, expected, result):
    assert_find_circle_num(result, expected)
    return


if __name__ == "__main__":
    app.run()
