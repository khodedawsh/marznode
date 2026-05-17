"""xray utilities"""

import re
import subprocess
from typing import Dict


def get_version(xray_path: str) -> str | None:
    """
    get xray version by running its executable
    :param xray_path:
    :return: xray version
    """
    cmd = [xray_path, "version"]
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
    match = re.match(r"^Xray (\d+\.\d+\.\d+)", output)
    if match:
        return match.group(1)
    return None


def get_x25519(xray_path: str, private_key: str = None) -> Dict[str, str] | None:
    """
    Calculates the public key from the provided private key.
    
    - Old output format ("Public key:")
    - New output format ("Password:")
    """

    cmd = [xray_path, "x25519"]
    if private_key:
        cmd.extend(["-i", private_key])
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode("utf-8")

    # Try New Format (v25.8.3+): Looks for "Password:" instead of Public Key
    match_new = re.match(r"PrivateKey:\s*(.+)\nPassword:\s*(.+)", output)
    if match_new:
        private, public = match_new.groups()
        return {"private_key": private, "public_key": public}

    # Try Old Format (< v25.8.3): Looks for standard "Public key:"
    match_old = re.match(r"Private key:\s*(.+)\nPublic key:\s*(.+)", output)
    if match_old:
        private, public = match_old.groups()
        return {"private_key": private, "public_key": public}

    return None
