import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_transfers, run_min_transfers
    from solution import Solution

    return Solution, assert_min_transfers, run_min_transfers


@app.cell
def _():
    # Example test case
    transactions = [[0, 1, 10], [2, 0, 5]]
    expected = 2
    return expected, transactions


@app.cell
def _(Solution, run_min_transfers, transactions):
    result = run_min_transfers(Solution, transactions)
    result
    return (result,)


@app.cell
def _(assert_min_transfers, expected, result):
    assert_min_transfers(result, expected)
    return


if __name__ == "__main__":
    app.run()
