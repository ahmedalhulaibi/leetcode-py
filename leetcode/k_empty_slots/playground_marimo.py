import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_k_empty_slots, run_k_empty_slots
    from solution import Solution

    return Solution, assert_k_empty_slots, run_k_empty_slots


@app.cell
def _():
    # Example test case
    bulbs = [1, 3, 2]
    k = 1
    expected = 2
    return bulbs, expected, k


@app.cell
def _(Solution, bulbs, k, run_k_empty_slots):
    result = run_k_empty_slots(Solution, bulbs, k)
    result
    return (result,)


@app.cell
def _(assert_k_empty_slots, expected, result):
    assert_k_empty_slots(result, expected)
    return


if __name__ == "__main__":
    app.run()
