# https://leetcode.com/problems/add-binary/

    def addBinary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a,2) + int(b,2)))[2:]