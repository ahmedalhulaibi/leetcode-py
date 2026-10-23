import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_fair_candy_swap, run_fair_candy_swap
    from solution import Solution

    return Solution, assert_fair_candy_swap, run_fair_candy_swap


@app.cell
def _():
    # Example test case
    alice_sizes = [1, 1]
    bob_sizes = [2, 2]
    expected = [1, 2]
    return alice_sizes, bob_sizes, expected


@app.cell
def _(Solution, alice_sizes, bob_sizes, run_fair_candy_swap):
    result = run_fair_candy_swap(Solution, alice_sizes, bob_sizes)
    result
    return (result,)


@app.cell
def _(assert_fair_candy_swap, expected, result):
    assert_fair_candy_swap(result, expected)
    return


if __name__ == "__main__":
    app.run()
