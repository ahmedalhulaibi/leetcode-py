import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_robot_bounded, run_is_robot_bounded
    from solution import Solution

    return Solution, assert_is_robot_bounded, run_is_robot_bounded


@app.cell
def _():
    # Example test case
    instructions = "GGLLGG"
    expected = True
    return expected, instructions


@app.cell
def _(Solution, instructions, run_is_robot_bounded):
    result = run_is_robot_bounded(Solution, instructions)
    result
    return (result,)


@app.cell
def _(assert_is_robot_bounded, expected, result):
    assert_is_robot_bounded(result, expected)
    return


if __name__ == "__main__":
    app.run()
