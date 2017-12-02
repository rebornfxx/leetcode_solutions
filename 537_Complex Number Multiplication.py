class Solution(object):
    def mine_complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x1, y1 = a.strip().split('+')
        x2, y2 = b.strip().split('+')
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1.replace('i',''))
        y2 = int(y2.replace('i',''))
        res = str(x1*x2-y1*y2) + '+' +str(x1*y2+x2*y1) + 'i'
        return res

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1, a2 = map(int, a[:-1].split('+'))
        b1, b2 = map(int, b[:-1].split('+'))
        return '%d+%di' % (a1 * b1 - a2 * b2, a1 * b2 + a2 * b1)