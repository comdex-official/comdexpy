from typing import Optional

LEDGER_RETURN_CODES = {
    "0x6400": "Execution error",
    "0x6700": "Wrong length",
    "0x6802": "Error deriving keys",
    "0x6982": "Empty buffer",
    "0x6983": "Output buffer too small",
    "0x6984": "Data is invalid",
    "0x6985": "Conditions not satisfied",
    "0x6986": "Command not allowed",
    "0x6a80": "Bad key handle",
    "0x6b00": "Invalid P1/P2",
    "0x6d00": "Instruction not supported",
    "0x6e00": "CLA not supported",
    "0x6f00": "Unknown",
    "0x6f01": "Sign/verify error",
    "0x9000": "Success",
    "0x9001": "Device is busy",
}


class ComdexPyError(Exception):
    pass


class ValueTooLargeError(ComdexPyError):
    pass


class EmptyMsgError(ComdexPyError):
    pass


class NotFoundError(ComdexPyError):
    pass


class UndefinedError(ComdexPyError):
    pass


class DecodeError(ComdexPyError):
    pass


class ConvertError(ComdexPyError):
    pass


class SchemaError(ComdexPyError):
    pass


class NotBip44Error(ComdexPyError):
    pass


class IncorrectLengthError(ComdexPyError):
    pass


class CosmosAppError(ComdexPyError):
    def __init__(self, return_code: Optional[str] = None):
        if return_code:
            self.msg = LEDGER_RETURN_CODES.get(return_code, "Unknown error")
        else:
            self.msg = "Unknown error"

    def __str__(self):
        return self.msg
