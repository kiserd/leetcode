# Author:       Donald Logan Kiser
# Date:         05/03/2022
# Description:  working through problem from Karat interview


counts = [
    '60,mail.sports.yahoo.com',
    '100,sports.yahoo.com',
    '200,yahoo.com',
    '50,silly.gov',
    '90,baseball.silly.gov',
    '75,england.uk',
    '150,england.com',
    '700,mailroom.google.com',
    '25,supernews.mailroom.google.com',
    '1000,bag.google.com',
    '120,newsoutlet.io',
    '111,silly.newsoutlet.io',
    '1,google.com',
    '25,scrum.england.uk',
]


def dhc(arr):
    # process each line of array into dict
    domain_hits = {}
    for s in arr:
        # split string into count and domain information
        count, domain_info = s.split(',')
        count = int(count)
        # parse domain info component
        curr = ''
        domain_info = domain_info.split('.')
        i = len(domain_info) - 1
        while i > -1:
            if not curr:
                curr += domain_info[i]
            else:
                curr = domain_info[i] + '.' + curr
            if curr in domain_hits:
                domain_hits[curr] += count
            else:
                domain_hits[curr] = count
            i -= 1
    return domain_hits

mapping = dhc(counts)
for key in mapping:
    print(f'{key}: {mapping[key]}')




