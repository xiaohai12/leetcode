class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        filename = []
        path_split = path.split('/')

        for Str in path_split:
            if Str == '..' and len(filename) != 0:
                filename.pop()
            elif Str == '' or Str == ' ' or Str == '.' or Str == '..':
                continue
            else:
                filename.append(Str)
        if filename == []:
            return '/'
        return '/' + '/'.join(filename)