import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_flipgame, run_flipgame
    from solution import Solution

    return Solution, assert_flipgame, run_flipgame


@app.cell
def _():
    # Example test case
    fronts: list[int] = [1, 2, 4, 4, 7]
    backs: list[int] = [1, 3, 4, 1, 3]
    expected = 2
    return backs, expected, fronts


@app.cell
def _(Solution, backs: list[int], fronts: list[int], run_flipgame):
    result = run_flipgame(Solution, fronts, backs)
    result
    return (result,)


@app.cell
def _(assert_flipgame, expected, result):
    assert_flipgame(result, expected)
    return


if __name__ == "__main__":
    app.run()
