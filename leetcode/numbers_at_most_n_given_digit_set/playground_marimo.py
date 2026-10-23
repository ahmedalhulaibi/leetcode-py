import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_at_most_n_given_digit_set, run_at_most_n_given_digit_set
    from solution import Solution

    return (
        Solution,
        assert_at_most_n_given_digit_set,
        run_at_most_n_given_digit_set,
    )


@app.cell
def _():
    # Example test case
    digits = ["1", "3", "5", "7"]
    n = 100
    expected = 20
    return digits, expected, n


@app.cell
def _(Solution, digits, n, run_at_most_n_given_digit_set):
    result = run_at_most_n_given_digit_set(Solution, digits, n)
    result
    return (result,)


@app.cell
def _(assert_at_most_n_given_digit_set, expected, result):
    assert_at_most_n_given_digit_set(result, expected)
    return


if __name__ == "__main__":
    app.run()
