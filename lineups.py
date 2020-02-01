import csv
from collections import Counter


class Lineup:
    entered_by = ''
    mvp = ''
    flex = []
    line = 0

    def __init__(self):
        self.flex = []

    def __str__(self):
        return "Entered By: " + self.entered_by + " MVP: " + self.mvp + " " + " Flex: " + self.flex.__str__()


personal_entries = []
lineups = []
lineups2 = []
with open('lineups.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        lineup = Lineup()
        lineup.entered_by = row["Entered By"]
        lineup.mvp = row["MVP"]
        lineup.flex.append(row["Flex1"])
        lineup.flex.append(row["Flex2"])
        lineup.flex.append(row["Flex3"])
        lineup.flex.append(row["Flex4"])
        lineup.line = line_count
        lineups.append(lineup)
        lineups2.append(lineup)
        line_count += 1

for lineup in lineups:
    personal_entries.append(lineup.entered_by)
    first = True
    lineup_a = lineup
    flex_a = lineup_a.flex
    for lineup_b in lineups2:
        flex_b = lineup_b.flex
        if set(flex_a) == set(flex_b):
            if lineup_a.mvp == lineup_b.mvp:
                if first:
                    first = False
                else:
                    print "Duplicate Found: "
                    print lineup_a
                    print lineup_b

# print personal_entries
c = Counter(personal_entries)
number_of_entries = len(personal_entries)

count = [(i, (c[i] / number_of_entries) * 100.0) for i in c.most_common()]
# print count

for i in c.most_common():
    percentage = (i[1] / float(number_of_entries)) * 100.0
    print i[0] + ": " + str(percentage)
