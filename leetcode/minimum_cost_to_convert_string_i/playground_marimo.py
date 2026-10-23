import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_cost, run_minimum_cost
    from solution import Solution

    return Solution, assert_minimum_cost, run_minimum_cost


@app.cell
def _():
    # Example test case
    source = "abcd"
    target = "acbe"
    original = ["a", "b", "c", "c", "e", "d"]
    changed = ["b", "c", "b", "e", "b", "e"]
    cost = [2, 5, 5, 1, 2, 20]
    expected = 28
    return changed, cost, expected, original, source, target


@app.cell
def _(Solution, changed, cost, original, run_minimum_cost, source, target):
    result = run_minimum_cost(Solution, source, target, original, changed, cost)
    result
    return (result,)


@app.cell
def _(assert_minimum_cost, expected, result):
    assert_minimum_cost(result, expected)
    return


if __name__ == "__main__":
    app.run()
