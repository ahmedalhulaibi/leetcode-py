import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_killed_enemies, run_max_killed_enemies
    from solution import Solution

    return Solution, assert_max_killed_enemies, run_max_killed_enemies


@app.cell
def _():
    # Example test case
    grid: list[list[str]] = [["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]
    expected = 3
    return expected, grid


@app.cell
def _(Solution, grid: list[list[str]], run_max_killed_enemies):
    result = run_max_killed_enemies(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_max_killed_enemies, expected, result):
    assert_max_killed_enemies(result, expected)
    return


if __name__ == "__main__":
    app.run()
