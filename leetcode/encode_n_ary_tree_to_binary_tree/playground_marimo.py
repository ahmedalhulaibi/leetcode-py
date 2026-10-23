import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_encode_decode_n_ary, run_encode_decode_n_ary
    from solution import Codec

    return Codec, assert_encode_decode_n_ary, run_encode_decode_n_ary


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, None, 3, 2, 4, None, 5, 6]
    return (root_list,)


@app.cell
def _(Codec, root_list: list[int | None], run_encode_decode_n_ary):
    result = run_encode_decode_n_ary(Codec, root_list)
    result
    return (result,)


@app.cell
def _(assert_encode_decode_n_ary, result, root_list: list[int | None]):
    assert_encode_decode_n_ary(result, root_list)
    return


if __name__ == "__main__":
    app.run()
