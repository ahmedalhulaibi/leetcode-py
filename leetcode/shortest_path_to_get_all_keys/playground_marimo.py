import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_path_all_keys, run_shortest_path_all_keys
    from solution import Solution

    return Solution, assert_shortest_path_all_keys, run_shortest_path_all_keys


@app.cell
def _():
    # Example test case
    grid = ["@.a..", "###.#", "b.A.B"]
    expected = 8
    return expected, grid


@app.cell
def _(Solution, grid, run_shortest_path_all_keys):
    result = run_shortest_path_all_keys(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_shortest_path_all_keys, expected, result):
    assert_shortest_path_all_keys(result, expected)
    return


if __name__ == "__main__":
    app.run()
