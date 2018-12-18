#PiOBD
from libs import netTCP #async connection modules contains send funcs
import request

# curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/bank/account/_bulk?pretty' --data-binary @accounts.json


if __name__ == "__main__":
    print("dupsko")