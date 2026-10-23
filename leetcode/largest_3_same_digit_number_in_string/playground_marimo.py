import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_good_integer, run_largest_good_integer
    from solution import Solution

    return Solution, assert_largest_good_integer, run_largest_good_integer


@app.cell
def _():
    # Example test case
    num = "6777133339"
    expected = "777"
    return expected, num


@app.cell
def _(Solution, num, run_largest_good_integer):
    result = run_largest_good_integer(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_largest_good_integer, expected, result):
    assert_largest_good_integer(result, expected)
    return


if __name__ == "__main__":
    app.run()
