from datetime import timedelta, datetime, date


class Dayscal: 
    def dayscalcu(self, startdate, enddate):
            startdate=date(self.startdate).day
            enddate=date(self.enddate).day
            diffrense=enddate-startdate
            return diffrense.days
diff=Dayscal()

diff.dayscalcu       

print(f'diffrence between your leave is:{diff}')