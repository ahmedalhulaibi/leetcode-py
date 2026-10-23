import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_has_group_size_x, run_has_group_size_x
    from solution import Solution

    return Solution, assert_has_group_size_x, run_has_group_size_x


@app.cell
def _():
    # Example test case
    deck = [1, 2, 3, 4, 4, 3, 2, 1]
    expected = True
    return deck, expected


@app.cell
def _(Solution, deck, run_has_group_size_x):
    result = run_has_group_size_x(Solution, deck)
    result
    return (result,)


@app.cell
def _(assert_has_group_size_x, expected, result):
    assert_has_group_size_x(result, expected)
    return


if __name__ == "__main__":
    app.run()
