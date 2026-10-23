import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_swap_pairs, run_swap_pairs
    from solution import Solution

    return Solution, assert_swap_pairs, run_swap_pairs


@app.cell
def _():
    # Example test case
    head_list = [1, 2, 3, 4]
    expected = [2, 1, 4, 3]
    return expected, head_list


@app.cell
def _(Solution, head_list, run_swap_pairs):
    result = run_swap_pairs(Solution, head_list)
    result
    return (result,)


@app.cell
def _(assert_swap_pairs, expected, result):
    assert_swap_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
