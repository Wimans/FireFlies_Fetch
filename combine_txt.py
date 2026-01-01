import pathlib

# Directory where your Fireflies txt files are stored
OUT_DIR = pathlib.Path("output")

# Output file
COMBINED = pathlib.Path("combined_transcripts.txt")

# --- OPTION A: combine *all* txt files ---
files = sorted(OUT_DIR.glob("*.txt"))

# --- OPTION B: OR select manually ---
# files = [
#     OUT_DIR / "Meeting_One_xyz123.txt",
#     OUT_DIR / "SomeOtherMeeting_abc987.txt",
# ]

with COMBINED.open("w", encoding="utf-8") as out:
    for f in files:
        text = f.read_text(encoding="utf-8").strip()

        out.write(f"{f.name}\n")
        out.write(text)
        out.write("\n\n" + "-" * 80 + "\n\n")  # separator (optional)

print("Done. Combined file saved as:", COMBINED.resolve())
