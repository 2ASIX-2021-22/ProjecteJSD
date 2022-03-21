"""
   The MIT License (MIT)

   Copyright (C) 2017-2020 Joe Testa (jtesta@positronsecurity.com)
   Copyright (C) 2017 Andris Raugulis (moo@arthepsy.eu)

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in
   all copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
   THE SOFTWARE.
"""
# pylint: disable=unused-import
from typing import Dict, List, Set, Sequence, Tuple, Iterable  # noqa: F401
from typing import Callable, Optional, Union, Any  # noqa: F401

from ssh_audit.ssh2_kexparty import SSH2_KexParty
from ssh_audit.readbuf import ReadBuf
from ssh_audit.writebuf import WriteBuf


class SSH2_Kex:
    def __init__(self, cookie: bytes, kex_algs: List[str], key_algs: List[str], cli: 'SSH2_KexParty', srv: 'SSH2_KexParty', follows: bool, unused: int = 0) -> None:
        self.__cookie = cookie
        self.__kex_algs = kex_algs
        self.__key_algs = key_algs
        self.__client = cli
        self.__server = srv
        self.__follows = follows
        self.__unused = unused

        self.__rsa_key_sizes: Dict[str, Tuple[int, int]] = {}
        self.__dh_modulus_sizes: Dict[str, Tuple[int, int]] = {}
        self.__host_keys: Dict[str, bytes] = {}

    @property
    def cookie(self) -> bytes:
        return self.__cookie

    @property
    def kex_algorithms(self) -> List[str]:
        return self.__kex_algs

    @property
    def key_algorithms(self) -> List[str]:
        return self.__key_algs

    # client_to_server
    @property
    def client(self) -> 'SSH2_KexParty':
        return self.__client

    # server_to_client
    @property
    def server(self) -> 'SSH2_KexParty':
        return self.__server

    @property
    def follows(self) -> bool:
        return self.__follows

    @property
    def unused(self) -> int:
        return self.__unused

    def set_rsa_key_size(self, rsa_type: str, hostkey_size: int, ca_size: int = -1) -> None:
        self.__rsa_key_sizes[rsa_type] = (hostkey_size, ca_size)

    def rsa_key_sizes(self) -> Dict[str, Tuple[int, int]]:
        return self.__rsa_key_sizes

    def set_dh_modulus_size(self, gex_alg: str, modulus_size: int) -> None:
        self.__dh_modulus_sizes[gex_alg] = (modulus_size, -1)

    def dh_modulus_sizes(self) -> Dict[str, Tuple[int, int]]:
        return self.__dh_modulus_sizes

    def set_host_key(self, key_type: str, hostkey: bytes) -> None:
        self.__host_keys[key_type] = hostkey

    def host_keys(self) -> Dict[str, bytes]:
        return self.__host_keys

    def write(self, wbuf: 'WriteBuf') -> None:
        wbuf.write(self.cookie)
        wbuf.write_list(self.kex_algorithms)
        wbuf.write_list(self.key_algorithms)
        wbuf.write_list(self.client.encryption)
        wbuf.write_list(self.server.encryption)
        wbuf.write_list(self.client.mac)
        wbuf.write_list(self.server.mac)
        wbuf.write_list(self.client.compression)
        wbuf.write_list(self.server.compression)
        wbuf.write_list(self.client.languages)
        wbuf.write_list(self.server.languages)
        wbuf.write_bool(self.follows)
        wbuf.write_int(self.__unused)

    @property
    def payload(self) -> bytes:
        wbuf = WriteBuf()
        self.write(wbuf)
        return wbuf.write_flush()

    @classmethod
    def parse(cls, payload: bytes) -> 'SSH2_Kex':
        buf = ReadBuf(payload)
        cookie = buf.read(16)
        kex_algs = buf.read_list()
        key_algs = buf.read_list()
        cli_enc = buf.read_list()
        srv_enc = buf.read_list()
        cli_mac = buf.read_list()
        srv_mac = buf.read_list()
        cli_compression = buf.read_list()
        srv_compression = buf.read_list()
        cli_languages = buf.read_list()
        srv_languages = buf.read_list()
        follows = buf.read_bool()
        unused = buf.read_int()
        cli = SSH2_KexParty(cli_enc, cli_mac, cli_compression, cli_languages)
        srv = SSH2_KexParty(srv_enc, srv_mac, srv_compression, srv_languages)
        kex = cls(cookie, kex_algs, key_algs, cli, srv, follows, unused)
        return kex
