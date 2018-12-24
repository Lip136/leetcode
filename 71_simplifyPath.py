class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        path = path.split('/')
        path = [i for i in path if i != '' and i != '.']
        for p in path:
            if p != '..':
                res.append(p)
            elif res:
                res.pop()
        return '/' + '/'.join(res)
