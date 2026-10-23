import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_robot_sim, run_robot_sim
    from solution import Solution

    return Solution, assert_robot_sim, run_robot_sim


@app.cell
def _():
    # Example test case
    commands = [4, -1, 4, -2, 4]
    obstacles = [[2, 4]]
    expected = 65
    return commands, expected, obstacles


@app.cell
def _(Solution, commands, obstacles, run_robot_sim):
    result = run_robot_sim(Solution, commands, obstacles)
    result
    return (result,)


@app.cell
def _(assert_robot_sim, expected, result):
    assert_robot_sim(result, expected)
    return


if __name__ == "__main__":
    app.run()
