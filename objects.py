import hashlib
import os
import json

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

def create_snapshot(filepaths: list[str]) -> dict:
    snapshot = {}

    # Store and hash each file 
    for path in filepaths:
        filehash = hash_and_store(path)
        snapshot[path] = filehash

    # turn dict -> JSON string -> bytes -> hash
    snapshot_str = json.dumps(snapshot, sort_keys=True)
    snapshot_bytes = snapshot_str.encode()
    snapshot_hash = hashlib.sha256(snapshot_bytes).hexdigest()

    # TODO: save `snapshot` dict as JSON somewhere in snapshots/

    os.makedirs("snapshots", exist_ok=True)

    with open(f"snapshots/{snapshot_hash}.json", "w") as f:
        json.dump(snapshot, f)

    # TODO: return something that identifies this snapshot
    
    return snapshot


if __name__ == "__main__":
    snap_id = create_snapshot(["testsave.txt"])
    print(snap_id)
    