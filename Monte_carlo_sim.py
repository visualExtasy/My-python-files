def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here
    import random
    lucky = 0.0
    for i in range(numTrials):
        bucket = ['R', 'R', 'R', 'R', 'G', 'G', 'G', 'G']
        a = bucket.pop(random.choice(range(len(bucket))))
        b = bucket.pop(random.choice(range(len(bucket))))
        c = bucket.pop(random.choice(range(len(bucket))))
        if a == b and a == c:
            lucky += 1
    return lucky / numTrials
