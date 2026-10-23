import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_design_tic_tac_toe, run_design_tic_tac_toe
    from solution import TicTacToe

    return TicTacToe, assert_design_tic_tac_toe, run_design_tic_tac_toe


@app.cell
def _():
    # Example test case
    operations = ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
    inputs = [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
    expected = [None, 0, 0, 0, 0, 0, 0, 1]
    return expected, inputs, operations


@app.cell
def _(TicTacToe, inputs, operations, run_design_tic_tac_toe):
    result, game = run_design_tic_tac_toe(TicTacToe, operations, inputs)
    print(result)
    game
    return (result,)


@app.cell
def _(assert_design_tic_tac_toe, expected, result):
    assert_design_tic_tac_toe(result, expected)
    return


if __name__ == "__main__":
    app.run()
