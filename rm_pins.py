import os
from pinata import Pinata
from dotenv import load_dotenv


load_dotenv()


pinata = Pinata(
    os.getenv("PINATA_API_KEY"),
    os.getenv("PINATA_API_SECRET_KEY"),
    os.getenv("PINATA_JWT"),
)


def remove_pins_from_pinata():
    response = pinata.get_pins()

    for _ in range(response["data"]["count"]):
        response = pinata.get_pins()

        for i in range(len(response["data"]["results"])):
            unpin_res = pinata.unpin_file(response["data"]["results"][i]["pin"]["cid"])
            print(unpin_res)

    print("Pinata Pins removed")


remove_pins_from_pinata()
