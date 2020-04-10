#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in  range(length):
        hash_table_insert(ht, weights[i], i)

    # Find the other weights to match limit?
    for i in range(length):
        # Finding the other weight amout that is needed to match the limit
        other_weight = limit - weights[i]
        # Check if the weight exists in hash table
        if hash_table_retrieve(ht, other_weight):
            # Return it tuple both indexes of the weights to match the limit
            the_index_of_other_weight = hash_table_retrieve(ht, other_weight)
            return (the_index_of_other_weight, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
