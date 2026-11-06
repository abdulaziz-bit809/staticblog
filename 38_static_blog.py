#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
38. Static Blog
Hayotiy amaliy loyiha
"""
import json, os
from datetime import datetime

FILE = "static_blog.json"

def load():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    data = load()
    print("="*40)
    print(f"  Static Blog")
    print("="*40)
    while True:
        print("\n1. Yangi yozuv")
        print("2. Royxat")
        print("3. Ochirish")
        print("4. Chiqish")
        c = input("Tanlang: ").strip()
        if c == "1":
            text = input("Malumot: ")
            data.append({"text": text, "date": datetime.now().strftime("%Y-%m-%d %H:%M")})
            save(data)
            print("✅ Qoshildi")
        elif c == "2":
            if not data: print("Bosh")
            for i, d in enumerate(data, 1):
                print(f"{i}. [{d['date']}] {d['text']}")
        elif c == "3":
            if data:
                idx = int(input("Raqam: ")) - 1
                if 0 <= idx < len(data):
                    data.pop(idx)
                    save(data)
                    print("✅ Ochirildi")
        elif c == "4":
            break

if __name__ == "__main__":
    main()
