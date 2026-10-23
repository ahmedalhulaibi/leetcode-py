import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_one_bit_character, run_is_one_bit_character
    from solution import Solution

    return Solution, assert_is_one_bit_character, run_is_one_bit_character


@app.cell
def _():
    # Example test case
    bits = [1, 0, 0]
    expected = True
    return bits, expected


@app.cell
def _(Solution, bits, run_is_one_bit_character):
    result = run_is_one_bit_character(Solution, bits)
    result
    return (result,)


@app.cell
def _(assert_is_one_bit_character, expected, result):
    assert_is_one_bit_character(result, expected)
    return


if __name__ == "__main__":
    app.run()
