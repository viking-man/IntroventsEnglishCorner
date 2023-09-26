import pytest
import time
from app.type import AudioType


def test_hash():
    message = "how to learn English?"
    s = str(hash(str(len(message))))
    print(s)

    print(str(int(time.time())))

    print(abs(hash(message)))

