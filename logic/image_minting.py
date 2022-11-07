import os
import requests
import json
from pathlib import Path
from pinata import Pinata
from dotenv import load_dotenv
from web3 import Web3


load_dotenv()


BASE_IPFS_URL = os.getenv("BASE_IPFS_URL")


def upload_img_to_ipfs(file_path: str) -> str:
    with Path(file_path).open("rb") as img:
        img_binary = img.read()
        ipfs_add_endpoint = "/api/v0/add"
        response = requests.post(
            BASE_IPFS_URL + ipfs_add_endpoint, files={"file": img_binary}
        )
        ipfs_hash = response.json()["Hash"]
        filename = file_path.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"

        return image_uri


PINATA_API_KEY = os.getenv("PINATA_API_KEY")
PINATA_API_SECRET_KEY = os.getenv("PINATA_API_SECRET_KEY")
PINATA_JWT = os.getenv("PINATA_JWT")


def upload_img_to_pinata(file_path: str) -> dict:
    pinata = Pinata(PINATA_API_KEY, PINATA_API_SECRET_KEY, PINATA_JWT)
    response = pinata.pin_file(file_path)

    return response


def upload_nft_metadata_to_pinata(
    nft_name: str, nft_description: str, image_uri: str
) -> str:
    nft_metadata_dict = {
        "name": nft_name,
        "description": nft_description,
        "image": image_uri,
    }
    with Path("nft_metadata.json").open("w") as fp:
        json.dump(nft_metadata_dict, fp)
    pinata = Pinata(PINATA_API_KEY, PINATA_API_SECRET_KEY, PINATA_JWT)
    response = pinata.pin_file("nft_metadata.json")
    metadata_ipfs_hash = response["data"]["IpfsHash"]
    pinned_metadata_url = f"https://gateway.pinata.cloud/ipfs/{metadata_ipfs_hash}"

    return pinned_metadata_url


def mint_collectable(tokenURI: str) -> None:
    tokenizer_erc20_address = "0x0D00624ce2C48542f036de97Edf736c64B0df53F"
    tokenizer_erc721_address = "0x970Af624fFF740E19dBDAFE0E0Ef4DB8eD53855c"
    tokenizer_erc721_abi = open("tokenizer_abi.json")
    w3_provider = Web3(Web3.HTTPProvider("HTTP://172.18.48.1:7545"))
    tokenizer_erc721_contract_instance = w3_provider.eth.contract(
        address=tokenizer_erc721_address,
        abi=json.loads(tokenizer_erc721_abi.read()),
    )
    tokenizer_erc721_contract_instance.functions.mintCollectable(
        tokenURI,
        tokenizer_erc20_address,
    ).transact(
        {
            "from": "0x23Aa2D6f49E69a32c017f78c3Bb9bdf066431074",
            "value": Web3.toWei(0.1, "ether"),
        }
    )
