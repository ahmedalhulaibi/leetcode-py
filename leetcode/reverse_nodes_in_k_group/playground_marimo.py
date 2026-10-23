import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reverse_k_group, run_reverse_k_group
    from solution import Solution

    return Solution, assert_reverse_k_group, run_reverse_k_group


@app.cell
def _():
    # Example test case
    head_vals = [1, 2, 3, 4, 5]
    k = 2
    expected_vals = [2, 1, 4, 3, 5]
    return expected_vals, head_vals, k


@app.cell
def _(Solution, head_vals, k, run_reverse_k_group):
    result = run_reverse_k_group(Solution, head_vals, k)
    result
    return (result,)


@app.cell
def _(assert_reverse_k_group, expected_vals, result):
    assert_reverse_k_group(result, expected_vals)
    return


if __name__ == "__main__":
    app.run()
