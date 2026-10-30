class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter = []
        digits = []
        for log in logs:
            identifier, content = log.split(" ", 1)
            if content[0].isdigit():
                digits.append(log)
            else:
                letter.append((content, identifier, log))
        
        letters_sorted = [x[2] for x in sorted(letter)]

        result = letters_sorted + digits
        return result