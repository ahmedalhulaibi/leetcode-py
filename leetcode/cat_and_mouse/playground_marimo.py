import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_cat_mouse_game, run_cat_mouse_game
    from solution import Solution

    return Solution, assert_cat_mouse_game, run_cat_mouse_game


@app.cell
def _():
    # Example test case
    graph = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]
    expected = 0
    return expected, graph


@app.cell
def _(Solution, graph, run_cat_mouse_game):
    result = run_cat_mouse_game(Solution, graph)
    result
    return (result,)


@app.cell
def _(assert_cat_mouse_game, expected, result):
    assert_cat_mouse_game(result, expected)
    return


if __name__ == "__main__":
    app.run()
