#!/usr/bin/env python3

from apollo.plugins.validation import PromptEngine


def run_console():
    p = PromptEngine()
    p.eval()


if __name__ == "__main__":
    run_console()
