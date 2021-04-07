#!/usr/bin/env python3

from cryptography.fernet import Fernet

import argparse

def main(keyfile):
    with open(keyfile, "rb") as f:
        key = f.read()

    cipher = Fernet(key)

    with open("latest", "rb") as f:
        data = f.read()

    enc = cipher.encrypt(data)

    with open("latest", "wb") as f:
        f.write(enc)

    print("[+] Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("keyfile")
    args = parser.parse_args()

    main(args.keyfile)

