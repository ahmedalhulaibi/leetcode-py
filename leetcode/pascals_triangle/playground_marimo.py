import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_generate, run_generate
    from solution import Solution

    return Solution, assert_generate, run_generate


@app.cell
def _():
    # Example test case
    num_rows: int = 5
    expected: list[list[int]] = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    return expected, num_rows


@app.cell
def _(Solution, num_rows: int, run_generate):
    result = run_generate(Solution, num_rows)
    result
    return (result,)


@app.cell
def _(assert_generate, expected: list[list[int]], result):
    assert_generate(result, expected)
    return


if __name__ == "__main__":
    app.run()
