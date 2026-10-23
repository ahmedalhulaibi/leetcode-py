import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_suggested_products, run_suggested_products
    from solution import Solution

    return Solution, assert_suggested_products, run_suggested_products


@app.cell
def _():
    # Example test case
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    search_word = "mouse"
    expected = [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
    ]
    return expected, products, search_word


@app.cell
def _(Solution, products, run_suggested_products, search_word):
    result = run_suggested_products(Solution, products, search_word)
    result
    return (result,)


@app.cell
def _(assert_suggested_products, expected, result):
    assert_suggested_products(result, expected)
    return


if __name__ == "__main__":
    app.run()
