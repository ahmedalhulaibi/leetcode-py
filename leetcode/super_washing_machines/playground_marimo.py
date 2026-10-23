import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_min_moves, run_find_min_moves
    from solution import Solution

    return Solution, assert_find_min_moves, run_find_min_moves


@app.cell
def _():
    # Example test case
    machines: list[int] = [1, 0, 5]
    expected = 3
    return expected, machines


@app.cell
def _(Solution, machines: list[int], run_find_min_moves):
    result = run_find_min_moves(Solution, machines)
    result
    return (result,)


@app.cell
def _(assert_find_min_moves, expected, result):
    assert_find_min_moves(result, expected)
    return


if __name__ == "__main__":
    app.run()
