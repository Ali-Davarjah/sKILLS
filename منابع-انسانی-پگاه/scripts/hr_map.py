#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نام قدیمیِ `map.py`. همان کار را می‌کند و هرچه بدهی به آن می‌سپارد.

    python hr_map.py table Personel      ==      python map.py table Personel

**در نوشته‌های تازه `map.py` را صدا بزن.** هر پنج اسکیلِ نقشه‌ی این خانواده
همان یک اسکریپت را دارند، پس دستورها و خروجی همه‌جا یکی است. این فایل فقط
برای این مانده که مسیرهای قدیمی نشکنند.
"""

import os
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(HERE, "map.py")

if __name__ == "__main__":
    sys.argv[0] = TARGET
    runpy.run_path(TARGET, run_name="__main__")
