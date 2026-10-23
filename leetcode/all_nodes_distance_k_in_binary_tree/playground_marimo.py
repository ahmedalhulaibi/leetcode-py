import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_distance_k, run_distance_k
    from solution import Solution

    return Solution, assert_distance_k, run_distance_k


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    target = 5
    k = 2
    expected = [7, 4, 1]
    return expected, k, root_list, target


@app.cell
def _(Solution, k, root_list: list[int | None], run_distance_k, target):
    result = run_distance_k(Solution, root_list, target, k)
    result
    return (result,)


@app.cell
def _(assert_distance_k, expected, result):
    assert_distance_k(result, expected)
    return


if __name__ == "__main__":
    app.run()
