import utils


text = "src/operations.json"
data = utils.open_file(text)
data = utils.check_state_and_sorted(data)

for i in utils.output_last_operations(data):
    print(i)
