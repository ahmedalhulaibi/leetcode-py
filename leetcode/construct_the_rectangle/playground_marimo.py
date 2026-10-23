import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_construct_rectangle, run_construct_rectangle
    from solution import Solution

    return Solution, assert_construct_rectangle, run_construct_rectangle


@app.cell
def _():
    # Example test case
    area = 4
    expected = [2, 2]
    return area, expected


@app.cell
def _(Solution, area, run_construct_rectangle):
    result = run_construct_rectangle(Solution, area)
    result
    return (result,)


@app.cell
def _(assert_construct_rectangle, expected, result):
    assert_construct_rectangle(result, expected)
    return


if __name__ == "__main__":
    app.run()
