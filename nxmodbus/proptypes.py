#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum

class PropType(Enum):
    SIGNAL          = 2
    BYTEARRAY       = 3
    STRING          = 4
    BOOL            = 5
    INT             = 6
    UINT            = 7
    FLOAT           = 8
    INT64           = 9
    UINT64          = 10
    FLOAT64         = 11
    ENUM            = 12
    BITFIELD        = 13
