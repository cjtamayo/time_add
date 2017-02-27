__author__ = 'Christian Tamayo'

def validator(listo):
    if type(listo) == str:
        listo = [listo]
    try:
        for time in listo:
            split = time.split(':')
            assert type(int(split[0])) == int
            assert type(int(split[1])) == int
            assert int(split[1]) < 60
            assert len(split[1]) == 2
        return True,
    except:
        return False, time

def time_subtract(time1, time2):
    if validator([time1,time2])[0]:
        if time1 == time2:
            return 0
        else:
            time1_tot = int(time1.split(':')[0]) * 60 + int(time1.split(':')[1])
            time2_tot = int(time2.split(':')[0]) * 60 + int(time2.split(':')[1])
            new_time = time1_tot - time2_tot
            if new_time < 0:
                return 'Time 1 must be greater than Time 2'
            new_time_min = str(new_time / 60)
            new_time_secs = str(new_time % 60)
            if len(new_time_secs) == 1:
                new_time_secs = '0' + new_time_secs
            return '{}:{}'.format(new_time_min, new_time_secs)
    else:
        return 'please enter valid times'

class Timer(object):

    def __init__(self):
        self.times = []

    def validate(self, listo):
        return validator(listo)[0]

    def show_times(self):
        if len(self.times) == 0:
            print 'No times have been entered'
        else:
            for time in self.times:
                print time

    def time_add(self,time):
        if self.validate(time):
            if type(time) == str:
                self.times.append(time)
            else:
                for times in time:
                    self.times.append(times)
        else:
            return '{} is not a valid time. Please try again'.format(validator(time)[1])

    def remove_time(self, out_time):
        if out_time in self.times:
            self.times.remove(out_time)
        else:
            print '{} has not been entered as a time'.format(out_time)

    def time_total(self):
        tot_mins = 0
        tot_secs = 0
        for times in self.times:
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
