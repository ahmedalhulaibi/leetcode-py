import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_successful_pairs, run_successful_pairs
    from solution import Solution

    return Solution, assert_successful_pairs, run_successful_pairs


@app.cell
def _():
    # Example test case
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    expected = [4, 0, 3]
    return expected, potions, spells, success


@app.cell
def _(Solution, potions, run_successful_pairs, spells, success):
    result = run_successful_pairs(Solution, spells, potions, success)
    result
    return (result,)


@app.cell
def _(assert_successful_pairs, expected, result):
    assert_successful_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
