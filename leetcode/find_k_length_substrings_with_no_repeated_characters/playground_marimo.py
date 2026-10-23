import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_k_len_substr_no_repeats, run_num_k_len_substr_no_repeats
    from solution import Solution

    return (
        Solution,
        assert_num_k_len_substr_no_repeats,
        run_num_k_len_substr_no_repeats,
    )


@app.cell
def _():
    # Example test case
    s = "havefunonleetcode"
    k = 5
    expected = 6
    return expected, k, s


@app.cell
def _(Solution, k, run_num_k_len_substr_no_repeats, s):
    result = run_num_k_len_substr_no_repeats(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_num_k_len_substr_no_repeats, expected, result):
    assert_num_k_len_substr_no_repeats(result, expected)
    return


if __name__ == "__main__":
    app.run()
