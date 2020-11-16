import hashlib


def hash_input(input):
    m = hashlib.sha256()
    m.update("message".encode("utf-8"))
    return m.hexdigest()


class Merkleroot(object):
    def __init__(self):
        pass

    def findMerkleRoot(self, leafHash):
        hash = []
        hash2 = []
        if len(leafHash) % 2 != 0:  ##if not even, repeat the last element
            leafHash.extend(leafHash[-1:])

        for leaf in sorted(leafHash):  ##for each leaf
            hash.append(leaf)
            if len(hash) % 2 == 0:  ##only add  hash if there are two first hash
                hash2.append(hash_input(hash[0] + hash[1]))  ##run through hash func for both hashes
                hash == []  ##reset first hash to empty
        if len(hash2) == 1:  ##if  hash is only one, we are the root
            return hash2
        else:
            return self.findMerkleRoot(hash2)  ##if not, recurse with hash2


def get_merkle_root(transactions):
    leafHash = []
    ##compute a list of hashes from transactions
    for trans in transactions:
        leafHash.append(hash_input(trans))

    mr = Merkleroot()
    return mr.findMerkleRoot(leafHash)


transactions = ['a', 'b', 'c','d']

print(get_merkle_root(transactions))