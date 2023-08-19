def is_impenetrable(expected_time, actual_time):
    """ 
    This function compares the expected time it will take to get from point a to point b
    with the actual time it took to get from point a to point b. If the explorers are late,
    the function returns True, otherwise it returns False.
    
    Parameters
    ----------
    expected_time: int
    actual_time: int
    
    Returns
    -------
    bool
        True if location_b is impenetrable, False otherwise   
    
    """

    expected_time_to_reach = expected_time + 60
    """Adding 60 minutes to the  expected time it will take to get from point a to point b"""

    if actual_time > expected_time_to_reach:
        return True
    else:
        return False