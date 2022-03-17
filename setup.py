# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="Estatus_Diario_Backup",
    version="1.0",
    description="monitoreo backup de respaldo de db",
    author="Jose Guillen",
    author_email="joseguillennavas@gmail.com",
    url="",
    license="MIT",
    scripts=["main.py"],
    console=["main.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)