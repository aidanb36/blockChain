"""
Example cryptocurrency miner

Constants:
+ REWARD: defines number of CatCoins miner receives per transaction
+ DIFFICULTY: Defines difficulty of problem to solve (higher number
    takes longer mining time). 5 is about right for this exercise.
+ DISPLAY: Print iterative test nonce values (True / False)
"""

import hashlib
from datetime import datetime as t
import csv
import sys

REWARD = 10
DIFFICULTY = 5
DISPLAY = True
MINER_WALLET_FILE = 'miner_wallet.csv'


def mining(previous_hash) -> tuple:
    """
    Perform mining work. Accept hash of previous block header and
    generate a new hash each iteration. Compare the first few chars
    (number of chars defined by DIFFICULTY constant) until a match is
    obtained. Purpose: demonstrate computational 'proof of work' for
    each transaction.
    :param previous_hash: str
    :return nonce: str, timestamp: datetime
    """

    start = t.now()
    to_hash = str(start).encode('utf-8')
    test_nonce = hashlib.sha256(to_hash).hexdigest()

    # while previous_hash[:DIFFICULTY] != test_nonce[:DIFFICULTY]:
    #     update = t.now()
    #     to_hash = str(update).encode('utf-8')
    #     test_nonce = hashlib.sha256(to_hash).hexdigest()
        # if DISPLAY:
        #    print(test_nonce)

    nonce = test_nonce
    timestamp = t.now()
    if DISPLAY:
        print("\nNonce:\n+", nonce)
        print(f"+ Mining difficulty: {DIFFICULTY}")
        print("+ Computational time:", timestamp - start)

    success = mining_reward(timestamp, nonce)
    if success:
        return nonce, timestamp
    else:
        print('Mining error. Aborting...')
        sys.exit()


def mining_reward(completed, nonce) -> bool:
    """
    Deposit mining reward (coins) into miner's wallet

    :param completed: datetime
    :param nonce: str
    :return bool
    """
    try:
        with open(MINER_WALLET_FILE, "a") as wallet:
            deposit = csv.writer(wallet)
            deposit.writerow([REWARD, completed, nonce])
        wallet.close()
    except IOError:
        print('Error reading file. Aborting...')
        sys.exit()
    else:
        return True


if __name__ == '__main__':
    # Run this to test the mining function:
    test_hash = '35bc0983b2a7907d1ce3da3c1163171aa927bf7ed959606fbc55c4e04432224e'
    n, t = mining(test_hash)
