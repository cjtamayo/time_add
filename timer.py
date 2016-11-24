__author__ = 'Christian Tamayo'

class Timer(object):

    def __init__(self):
        self.times = []

    def show_times(self):
        print self.times

    def time_add(self,time):
        self.times.append(time)

    def time_remove(self, out_time):
        if out_time in self.times:
            self.times.remove(out_time)

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

    def time_subtract(self, time1, time2):
        #this needs to be filled!
        pass
