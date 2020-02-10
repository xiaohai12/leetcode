class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        Name = self.count(name)
        Type = self.count(typed)
        if len(Name) > len(Type):
            return False
        for i in range(len(Name)):
            if Name[i][0] == Type[i][0] and Name[i][1] <= Type[i][1]:
                continue
            else:
                return False
        return True

    def count(self, S):
        end = []
        rec = (S[0], 0)
        for s in S:
            if s == rec[0]:
                rec = (s, rec[1] + 1)
            else:
                end.append(rec)
                rec = (s, 1)
        end.append(rec)
        return end

