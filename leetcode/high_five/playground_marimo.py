import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_high_five, run_high_five
    from solution import Solution

    return Solution, assert_high_five, run_high_five


@app.cell
def _():
    # Example test case
    items = [
        [1, 91],
        [1, 92],
        [2, 93],
        [2, 97],
        [1, 60],
        [2, 77],
        [1, 65],
        [1, 87],
        [1, 100],
        [2, 100],
        [2, 76],
    ]
    expected = [[1, 87], [2, 88]]
    return expected, items


@app.cell
def _(Solution, items, run_high_five):
    result = run_high_five(Solution, items)
    result
    return (result,)


@app.cell
def _(assert_high_five, expected, result):
    assert_high_five(result, expected)
    return


if __name__ == "__main__":
    app.run()
