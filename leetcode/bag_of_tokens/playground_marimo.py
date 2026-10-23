import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_bag_of_tokens_score, run_bag_of_tokens_score
    from solution import Solution

    return Solution, assert_bag_of_tokens_score, run_bag_of_tokens_score


@app.cell
def _():
    # Example test case
    tokens = [100, 200, 300, 400]
    power = 200
    expected = 2
    return expected, power, tokens


@app.cell
def _(Solution, power, run_bag_of_tokens_score, tokens):
    result = run_bag_of_tokens_score(Solution, tokens, power)
    result
    return (result,)


@app.cell
def _(assert_bag_of_tokens_score, expected, result):
    assert_bag_of_tokens_score(result, expected)
    return


if __name__ == "__main__":
    app.run()
