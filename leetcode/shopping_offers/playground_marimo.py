import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shopping_offers, run_shopping_offers
    from solution import Solution

    return Solution, assert_shopping_offers, run_shopping_offers


@app.cell
def _():
    # Example test case
    price = [2, 5]
    special = [[3, 0, 5], [1, 2, 10]]
    needs = [3, 2]
    expected = 14
    return expected, needs, price, special


@app.cell
def _(Solution, needs, price, run_shopping_offers, special):
    result = run_shopping_offers(Solution, price, special, needs)
    result
    return (result,)


@app.cell
def _(assert_shopping_offers, expected, result):
    assert_shopping_offers(result, expected)
    return


if __name__ == "__main__":
    app.run()
