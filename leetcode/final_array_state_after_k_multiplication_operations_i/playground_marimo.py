import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_final_state, run_get_final_state
    from solution import Solution

    return Solution, assert_get_final_state, run_get_final_state


@app.cell
def _():
    # Example test case
    nums = [2, 1, 3, 5, 6]
    k = 5
    multiplier = 2
    expected = [8, 4, 6, 5, 6]
    return expected, k, multiplier, nums


@app.cell
def _(Solution, k, multiplier, nums, run_get_final_state):
    result = run_get_final_state(Solution, nums, k, multiplier)
    result
    return (result,)


@app.cell
def _(assert_get_final_state, expected, result):
    assert_get_final_state(result, expected)
    return


if __name__ == "__main__":
    app.run()
