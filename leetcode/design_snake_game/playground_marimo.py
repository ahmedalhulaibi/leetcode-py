import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_design_snake_game, run_design_snake_game
    from solution import SnakeGame

    return SnakeGame, assert_design_snake_game, run_design_snake_game


@app.cell
def _():
    # Example test case
    operations = ["SnakeGame", "move", "move", "move", "move", "move", "move"]
    inputs = [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
    expected = [None, 0, 0, 1, 1, 2, -1]
    return expected, inputs, operations


@app.cell
def _(SnakeGame, inputs, operations, run_design_snake_game):
    result, game = run_design_snake_game(SnakeGame, operations, inputs)
    print(result)
    game
    return (result,)


@app.cell
def _(assert_design_snake_game, expected, result):
    assert_design_snake_game(result, expected)
    return


if __name__ == "__main__":
    app.run()
