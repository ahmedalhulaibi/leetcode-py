import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_prime_sub_operation, run_prime_sub_operation
    from solution import Solution

    return Solution, assert_prime_sub_operation, run_prime_sub_operation


@app.cell
def _():
    # Example test case
    nums = [4, 9, 6, 10]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_prime_sub_operation):
    result = run_prime_sub_operation(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_prime_sub_operation, expected, result):
    assert_prime_sub_operation(result, expected)
    return


if __name__ == "__main__":
    app.run()
