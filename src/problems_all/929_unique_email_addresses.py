
def unique(emails):
    data = {}
    for email in emails:
        s = email.split('@')
        local = s[0].split('+')
        local = local[0]
        local = local.replace('.', '')
        if s[1] not in data:
            data[s[1]] = set()

        data[s[1]].add(local)
    
    total = 0
    for email in data:
        total += len(data[email])

    return total


if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    total = unique(emails)
    print(total)

