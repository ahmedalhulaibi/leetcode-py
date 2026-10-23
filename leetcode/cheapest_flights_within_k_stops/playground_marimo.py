import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_cheapest_price, run_find_cheapest_price
    from solution import Solution

    return Solution, assert_find_cheapest_price, run_find_cheapest_price


@app.cell
def _():
    # Example test case
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1
    expected = 700
    return dst, expected, flights, k, n, src


@app.cell
def _(Solution, dst, flights, k, n, run_find_cheapest_price, src):
    result = run_find_cheapest_price(Solution, n, flights, src, dst, k)
    result
    return (result,)


@app.cell
def _(assert_find_cheapest_price, expected, result):
    assert_find_cheapest_price(result, expected)
    return


if __name__ == "__main__":
    app.run()
