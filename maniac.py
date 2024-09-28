#package for main py

import discord

import os

import asyncio

import yt_dlp

from dotenv import load_dotenv

def run_bot():
    load_dotenv()
    TOKEN = os.getenv('discord_token')