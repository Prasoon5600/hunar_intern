def find_runner_up_score(scores):
    # Convert the list to a set to remove duplicates
    unique_scores = list(set(scores))
    # Sort the scores in descending order
    unique_scores.sort(reverse=True)
    # The runner-up score will be the second item in the sorted list
    runner_up_score = unique_scores[1]
    return runner_up_score

# Example:
scores = [45, 67, 89, 90, 67, 89, 90, 100]
runner_up = find_runner_up_score(scores)
print(f"The runner-up score is: {runner_up}")


