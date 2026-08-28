import hashlib
import os

def hash_and_store(filepath: str) -> str:
    # read the file's bytes
    with open(filepath, "rb") as f:

        # raw file as bytes
        data = f.read()

        # compute a SHA-1 or SHA-256 hash of those bytes
        filehash = hashlib.sha256(data).hexdigest()

        # make objects dir if doesn't exist
        os.makedirs("objects", exist_ok=True)

        # write the bytes to ./objects/<hash>
        with open(f"objects/{filehash}", "wb") as out:
            out.write(data)

        return filehash

if __name__ == "__main__":
    h = hash_and_store("testsave.txt")
    print(h)
    