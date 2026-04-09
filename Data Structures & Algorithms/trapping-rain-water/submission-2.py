class Solution:
    def trap(self, h):
        n = len(h)
        res = 0
        l = 0

        while l < n - 1:
            if h[l] == 0:
                l += 1
                continue

            # cherche le prochain mur au moins aussi haut que h[l]
            r = l + 1
            while r < n and h[r] < h[l]:
                r += 1

            if r == n:
                # pas de mur aussi haut → prend le plus haut restant
                r = l + 1
                for i in range(l + 2, n):
                    if h[i] > h[r]:
                        r = i

            # calcule l'eau entre les deux murs
            level = min(h[l], h[r])
            for i in range(l + 1, r):
                res += max(0, level - h[i])

            l = r

        return res