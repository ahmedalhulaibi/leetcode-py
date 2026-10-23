import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_k_divisible_components, run_max_k_divisible_components
    from solution import Solution

    return (
        Solution,
        assert_max_k_divisible_components,
        run_max_k_divisible_components,
    )


@app.cell
def _():
    # Example test case
    n = 5
    edges = [[0, 2], [1, 2], [1, 3], [2, 4]]
    values = [1, 8, 1, 4, 4]
    k = 6
    expected = 2
    return edges, expected, k, n, values


@app.cell
def _(Solution, edges, k, n, run_max_k_divisible_components, values):
    result = run_max_k_divisible_components(Solution, n, edges, values, k)
    result
    return (result,)


@app.cell
def _(assert_max_k_divisible_components, expected, result):
    assert_max_k_divisible_components(result, expected)
    return


if __name__ == "__main__":
    app.run()
