import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_linked_list_ops, run_linked_list_ops
    from solution import MyLinkedList

    return MyLinkedList, assert_linked_list_ops, run_linked_list_ops


@app.cell
def _():
    # Example test case
    operations = [
        "MyLinkedList",
        "add_at_head",
        "add_at_tail",
        "add_at_index",
        "get",
        "delete_at_index",
        "get",
    ]
    inputs = [[], [1], [3], [1, 2], [1], [1], [1]]
    expected = [None, None, None, None, 2, None, 3]
    return expected, inputs, operations


@app.cell
def _(MyLinkedList, inputs, operations, run_linked_list_ops):
    result, linked_list = run_linked_list_ops(MyLinkedList, operations, inputs)
    print(result)
    linked_list
    return (result,)


@app.cell
def _(assert_linked_list_ops, expected, result):
    assert_linked_list_ops(result, expected)
    return


if __name__ == "__main__":
    app.run()
