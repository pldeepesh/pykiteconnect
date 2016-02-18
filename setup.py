#!/usr/bin/env python

from setuptools import setup

setup(
	name="kiteconnect",
	version="2.4.2",
	description="The official Python client for the Kite Connect trading API",
	author="Rainmatter Technology (India)",
	author_email="talk@rainmatter.com",
	url="https://kite.trade",
	packages=["kiteconnect"],
	download_url="https://github.com/rainmattertech/pykiteconnect",
	license="MIT",
	classifiers=[
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Intended Audience :: Financial and Insurance Industry",
		"Programming Language :: Python",
		"Natural Language :: English",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		"Topic :: Office/Business :: Financial :: Investment",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Software Development :: Libraries"
	],
	install_requires=["requests"]
)
