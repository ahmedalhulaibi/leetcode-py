import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_insert_greatest_common_divisors, run_insert_greatest_common_divisors
    from solution import Solution

    return (
        Solution,
        assert_insert_greatest_common_divisors,
        run_insert_greatest_common_divisors,
    )


@app.cell
def _():
    # Example test case
    head_list = [18, 6, 10, 3]
    expected_list = [18, 6, 6, 2, 10, 1, 3]
    return expected_list, head_list


@app.cell
def _(Solution, head_list, run_insert_greatest_common_divisors):
    result = run_insert_greatest_common_divisors(Solution, head_list)
    result
    return (result,)


@app.cell
def _(assert_insert_greatest_common_divisors, expected_list, result):
    assert_insert_greatest_common_divisors(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
