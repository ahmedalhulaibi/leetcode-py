import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_transactions, run_max_transactions
    from solution import Solution

    return Solution, assert_max_transactions, run_max_transactions


@app.cell
def _():
    # Example test case
    transactions = [2, -5, 3, -1, -2]
    expected = 4
    return expected, transactions


@app.cell
def _(Solution, run_max_transactions, transactions):
    result = run_max_transactions(Solution, transactions)
    result
    return (result,)


@app.cell
def _(assert_max_transactions, expected, result):
    assert_max_transactions(result, expected)
    return


if __name__ == "__main__":
    app.run()
