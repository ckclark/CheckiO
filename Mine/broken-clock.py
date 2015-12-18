import re
from datetime import datetime, timedelta
def broken_clock(starting_time, wrong_time, error_description):
    starting_time = datetime.strptime(starting_time, '%H:%M:%S')
    wrong_time = datetime.strptime(wrong_time, '%H:%M:%S')
    diff = (wrong_time - starting_time).seconds
    mat = re.match(r'([+-]\d+) (.)(?:econd|inute|our)s? at (\d+) (.)(?:econd|inute|our)s?', error_description)
    ediff, eduration = int(mat.group(1)), int(mat.group(3))
    ediff *= dict(s=1, m=60, h=3600)[mat.group(2)]
    eduration *= dict(s=1, m=60, h=3600)[mat.group(4)]
    real_offset = int(float(diff) * eduration / (eduration + ediff))
    return (starting_time + timedelta(seconds=real_offset)).strftime('%H:%M:%S')

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
