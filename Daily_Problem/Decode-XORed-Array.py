class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # encoded[i] = arr[i] XOR arr[i + 1]
        # arr[i + 1] = arr[i] XOR encoded[i]
        # We knoe the arr[i]
        arr = [first]
        for i in range(len(encoded)):
            arr.append(encoded[i] ^ arr[i])
        return arr

        