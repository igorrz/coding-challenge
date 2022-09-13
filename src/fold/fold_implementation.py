from email import iterators
import functools


def fold(folding_funct, input_sequence, starting_value = None, fold_type = 'left'):
    """Implementation of the fold function. This function takes an iterable of type A, a starting value of type B, 
    a function of a type fct(A,B)->B and returns B.
    
    Args: 
        folding_funct: the function representing the combining operation for the fold function
        input_sequence: the sequence to be folded
        starting_value: the starting value of the fold
        fold_type: the type of the fold operation. Defaults to left.
    Returns:
        result: the output of the folding operation.
    """


    if not input_sequence:
        raise ValueError('The input sequence can not be empty')
    
    # Transfrom the sequence to an iterable element
    iterable = iter(input_sequence)

    # If right fold, invert the iterable
    if fold_type == 'right':
        iterable = [x for x in iterable].reverse()
        iterable = iter(iterable)
    
    # initialize the starting value, if none is given
    if starting_value is None:
        starting_value = next(iterable)
    
    result = starting_value
    _ = [result := folding_funct(x, result) for x in iterable]

    return result