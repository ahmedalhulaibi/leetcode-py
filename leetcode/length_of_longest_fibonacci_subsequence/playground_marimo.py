import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_len_longest_fib_subsequence, run_len_longest_fib_subsequence
    from solution import Solution

    return (
        Solution,
        assert_len_longest_fib_subsequence,
        run_len_longest_fib_subsequence,
    )


@app.cell
def _():
    # Example test case
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    expected = 5
    return arr, expected


@app.cell
def _(Solution, arr, run_len_longest_fib_subsequence):
    result = run_len_longest_fib_subsequence(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_len_longest_fib_subsequence, expected, result):
    assert_len_longest_fib_subsequence(result, expected)
    return


if __name__ == "__main__":
    app.run()
