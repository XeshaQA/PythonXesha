def count_pass_recursive(test_results):
    if not test_results:
        return 0

    first_element = test_results[0]
    if first_element == 'PASS':
        return 1 + count_pass_recursive(test_results[1:])
    else:
        return count_pass_recursive(test_results[1:])
results = ['PASS', 'FAIL', 'PASS', 'SKIP', 'PASS', 'FAIL']
print(count_pass_recursive(results))
