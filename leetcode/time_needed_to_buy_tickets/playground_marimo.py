import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_time_required_to_buy, run_time_required_to_buy
    from solution import Solution

    return Solution, assert_time_required_to_buy, run_time_required_to_buy


@app.cell
def _():
    # Example test case
    tickets = [2, 3, 2]
    k = 2
    expected = 6
    return expected, k, tickets


@app.cell
def _(Solution, k, run_time_required_to_buy, tickets):
    result = run_time_required_to_buy(Solution, tickets, k)
    result
    return (result,)


@app.cell
def _(assert_time_required_to_buy, expected, result):
    assert_time_required_to_buy(result, expected)
    return


if __name__ == "__main__":
    app.run()
