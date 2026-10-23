import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_closest_k_values, run_closest_k_values
    from solution import Solution

    return Solution, assert_closest_k_values, run_closest_k_values


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [4, 2, 5, 1, 3]
    target = 3.714286
    k = 2
    expected = [3, 4]
    return expected, k, root_list, target


@app.cell
def _(Solution, k, root_list: list[int | None], run_closest_k_values, target):
    result = run_closest_k_values(Solution, root_list, target, k)
    result
    return (result,)


@app.cell
def _(assert_closest_k_values, expected, result):
    assert_closest_k_values(result, expected)
    return


if __name__ == "__main__":
    app.run()
