class Solution:
    def carFleet(self, target, position, speed):
        pairs = sorted(zip(position, speed), reverse=True)
        res = 0
        prev_time = 0
        for pos, spd in pairs:
            time = (target - pos) / spd
            if time > prev_time:   # cette voiture n'est rattrapée par personne devant
                res += 1
                prev_time = time
        return res