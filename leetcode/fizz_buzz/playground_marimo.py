import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_fizz_buzz, run_fizz_buzz
    from solution import Solution

    return Solution, assert_fizz_buzz, run_fizz_buzz


@app.cell
def _():
    # Example test case
    n = 5
    expected = ["1", "2", "Fizz", "4", "Buzz"]
    return expected, n


@app.cell
def _(Solution, n, run_fizz_buzz):
    result = run_fizz_buzz(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_fizz_buzz, expected, result):
    assert_fizz_buzz(result, expected)
    return


if __name__ == "__main__":
    app.run()
