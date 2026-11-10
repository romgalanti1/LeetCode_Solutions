class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self,i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self,i,j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False # already unioned

        if self.rank[root_i] < self.rank[root_j]:
            root_i, root_j = root_j, root_i
        
        self.parent[root_j] = root_i
        if self.rank[root_i] == self.rank[root_j]:
            self.rank[root_i] += 1

        return True
    
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        n = len(accounts)
        dsu = DSU(n)
        email_to_acc = {}
        # attach same emails to same account index
        for i,acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_to_acc:
                    dsu.union(i,email_to_acc[email])
                else:
                    email_to_acc[email] = i

        root_to_emails = defaultdict(list)
        for email, acc_index in email_to_acc.items():
            root = dsu.find(acc_index)
            root_to_emails[root].append(email)
        
        output = []
        for index, emails in root_to_emails.items():
            name = accounts[index][0]
            output.append([name] + sorted(emails))
        
        return output
