import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_detect_cycle, run_detect_cycle
    from solution import Solution

    return Solution, assert_detect_cycle, run_detect_cycle


@app.cell
def _():
    # Example test case
    head_vals: list[int] = [3, 2, 0, -4]
    pos: int = 1
    expected: int = 1
    return expected, head_vals, pos


@app.cell
def _(Solution, head_vals: list[int], pos: int, run_detect_cycle):
    result = run_detect_cycle(Solution, head_vals, pos)
    print(f"Cycle starts at index: {result}")
    result
    return (result,)


@app.cell
def _(assert_detect_cycle, expected: int, result):
    assert_detect_cycle(result, expected)
    return


if __name__ == "__main__":
    app.run()
