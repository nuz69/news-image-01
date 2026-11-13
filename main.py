#!/usr/bin/env python3
import pathlib

def main():
    script_dir = pathlib.Path(__file__).resolve().parent
    src_path = script_dir / "image.jpg"
    output_dir = pathlib.Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    dst_path = output_dir / "entry.png"
    dst_path.write_bytes(src_path.read_bytes())

if __name__ == "__main__":
    main()
