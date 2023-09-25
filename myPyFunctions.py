''' Collect some useful self-defined python functions '''

def count_csv_rows(file):
    ''' Count the record/row numbers in a csv file
    Header is included.
    file should include the path as well.

    Zhiyong Wu 2023/09
    '''

    import csv

    # Setting initial value of the counter to zero
    ict = 0

    # iterating through the whole file
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            ict += 1

    return ict

def create_num_list(iranges):
    '''
    Create a list of numbers with the given ranges (inclusive)
    iranges = [(istart1, iend1), (istart2, iend2), ...]

    Zhiyong Wu 2023/09
    '''

    # intiate the number list
    numbers = []

    for irange in iranges:
        for i in list(itertools.chain(range(irange[0], irange[1]+1))):
            numbers.append(i)

    return numbers