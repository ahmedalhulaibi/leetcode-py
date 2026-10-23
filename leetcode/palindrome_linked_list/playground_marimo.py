import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_palindrome, run_is_palindrome
    from solution import Solution

    return Solution, assert_is_palindrome, run_is_palindrome


@app.cell
def _():
    # Example test case
    head_list = [1, 2, 2, 1]
    expected = True
    return expected, head_list


@app.cell
def _(Solution, head_list, run_is_palindrome):
    result = run_is_palindrome(Solution, head_list)
    result
    return (result,)


@app.cell
def _(assert_is_palindrome, expected, result):
    assert_is_palindrome(result, expected)
    return


if __name__ == "__main__":
    app.run()
