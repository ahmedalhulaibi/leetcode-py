import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_calculate_minimum_hp, run_calculate_minimum_hp
    from solution import Solution

    return Solution, assert_calculate_minimum_hp, run_calculate_minimum_hp


@app.cell
def _():
    # Example test case
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    expected = 7
    return dungeon, expected


@app.cell
def _(Solution, dungeon, run_calculate_minimum_hp):
    result = run_calculate_minimum_hp(Solution, dungeon)
    result
    return (result,)


@app.cell
def _(assert_calculate_minimum_hp, expected, result):
    assert_calculate_minimum_hp(result, expected)
    return


if __name__ == "__main__":
    app.run()
