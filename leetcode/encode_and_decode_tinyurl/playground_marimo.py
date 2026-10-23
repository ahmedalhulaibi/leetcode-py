import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_encode_and_decode_tinyurl, run_encode_and_decode_tinyurl
    from solution import Codec

    return (
        Codec,
        assert_encode_and_decode_tinyurl,
        run_encode_and_decode_tinyurl,
    )


@app.cell
def _():
    # Example test case
    operations = ["Codec", "encode", "decode"]
    inputs = [[""], ["https://leetcode.com/problems/design-tinyurl"], []]
    expected = [None, None, "https://leetcode.com/problems/design-tinyurl"]
    return expected, inputs, operations


@app.cell
def _(Codec, inputs, operations, run_encode_and_decode_tinyurl):
    result, codec = run_encode_and_decode_tinyurl(Codec, operations, inputs)
    print(result)
    codec
    return (result,)


@app.cell
def _(assert_encode_and_decode_tinyurl, expected, result):
    assert_encode_and_decode_tinyurl(result, expected)
    return


if __name__ == "__main__":
    app.run()
