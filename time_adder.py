__author__ = 'Christian Tamayo'

def loopstart():
    timetime = []
    while True:
        timething = raw_input('What is your time? Enter time, "done", "remove" or "reset"\n')
        if timething.upper() == 'DONE':
            break
        elif timething.upper() == 'RESET':
            timetime = []
        elif timething.upper() == 'REMOVE':
            try:
                timetime.pop()
            except:
                print 'Nothing to remove\n'
                continue
        else:
            try:
                split = timething.split(':')
                assert type(int(split[0])) == int
                assert type(int(split[1])) == int
                timetime.append(timething)
            except Exception as e:
                print 'Please enter a valid time'
                continue
    return timetime

def time_add(time_list):
    tot_mins = 0
    tot_secs = 0
    for times in time_list:
        split = times.split(':')
        tot_mins += int(split[0])
        tot_secs += int(split[1])
    tot_mins += tot_secs/60
    secs = str(tot_secs%60)
    if len(secs) == 1:
        secs = '0' + secs
    if tot_mins >= 60:
        new_tot_mins = tot_mins/60
        new_new_tm = str(tot_mins - new_tot_mins*60)
        if len(new_new_tm) == 1:
            new_new_tm = '0'+ new_new_tm
        return str(new_tot_mins) + ':' + new_new_tm + ':' + secs
    else:
        return str(tot_mins) + ':' + secs

def main():
    print '\nTotal time is: ' + time_add(loopstart())

if __name__ == '__main__':
    main()
