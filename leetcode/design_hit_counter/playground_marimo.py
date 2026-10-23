import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_hit_counter, run_hit_counter
    from solution import HitCounter

    return HitCounter, assert_hit_counter, run_hit_counter


@app.cell
def _():
    # Example test case
    operations = ["HitCounter", "hit", "hit", "hit", "get_hits", "hit", "get_hits", "get_hits"]
    inputs = [[], [1], [2], [3], [4], [300], [300], [301]]
    expected = [None, None, None, None, 3, None, 4, 3]
    return expected, inputs, operations


@app.cell
def _(HitCounter, inputs, operations, run_hit_counter):
    result, counter = run_hit_counter(HitCounter, operations, inputs)
    print(result)
    counter
    return (result,)


@app.cell
def _(assert_hit_counter, expected, result):
    assert_hit_counter(result, expected)
    return


if __name__ == "__main__":
    app.run()
