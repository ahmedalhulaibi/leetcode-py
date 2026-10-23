import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_lemonade_change, run_lemonade_change
    from solution import Solution

    return Solution, assert_lemonade_change, run_lemonade_change


@app.cell
def _():
    # Example test case
    bills = [5, 5, 5, 10, 20]
    expected = True
    return bills, expected


@app.cell
def _(Solution, bills, run_lemonade_change):
    result = run_lemonade_change(Solution, bills)
    result
    return (result,)


@app.cell
def _(assert_lemonade_change, expected, result):
    assert_lemonade_change(result, expected)
    return


if __name__ == "__main__":
    app.run()
