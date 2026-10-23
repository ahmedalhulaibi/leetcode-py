import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_escape_ghosts, run_escape_ghosts
    from solution import Solution

    return Solution, assert_escape_ghosts, run_escape_ghosts


@app.cell
def _():
    # Example test case
    ghosts: list[list[int]] = [[1, 0], [0, 3]]
    target: list[int] = [0, 1]
    expected = True
    return expected, ghosts, target


@app.cell
def _(Solution, ghosts: list[list[int]], run_escape_ghosts, target: list[int]):
    result = run_escape_ghosts(Solution, ghosts, target)
    result
    return (result,)


@app.cell
def _(assert_escape_ghosts, expected, result):
    assert_escape_ghosts(result, expected)
    return


if __name__ == "__main__":
    app.run()
