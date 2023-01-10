# Every valid email consists of a local name and a domain name, separated by the '@' sign.
# Besides lowercase letters, the email may contain one or more '.' or '+'.

# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address,
# mail sent there will be forwarded to the same address without dots in the local name.
# Note that this rule does not apply to domain names.

# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored.
# This allows certain emails to be filtered. Note that this rule does not apply to domain names.

# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.

# Given an array of strings emails where we send one email to each emails[i],
# return the number of different addresses that actually receive mails.

# example
# emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
# Output = 3

# emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2

# optimized the code to use a set instead of a list
# set is by nature having unique elements so the size of the set will be number of unique emails
# if list is used, a check should be made while appending the email to the list. the check if the email to append already exists in the list,
# makes a list lookup which increases the time complexity

def numUniqueEmails(emails: list[str]) -> int:
    valid_emails = set()
    for email in emails:
        e_parts = email.split('@')
        localname = e_parts[0]
        index = localname.find('+')
        if index > -1:
            localname = localname[:index]
        localname = localname.replace('.', '')
        valid_emails.add(localname + '@' + e_parts[1])

    return len(valid_emails)


if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(numUniqueEmails(emails))
    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    print(numUniqueEmails(emails))
